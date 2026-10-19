import copy
from datetime import datetime, timedelta, timezone
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import release_registry as r


def manifest(aid='desktop', assets=None):
    data = json.loads((ROOT / 'registry/applications.json').read_text())
    base = copy.deepcopy(next(a for a in data['applications'] if a['id'] == 'desktop'))
    base['id'] = aid
    base.update(version='1.0.0', version_code=None, release_status='published',
                provenance={'run_id':1, 'run_attempt':1, 'head_sha':'a'*40,'artifact_id':10,'workflow':'.github/workflows/windows-build.yml'})
    if assets:
        base['installers'] = assets
    for index, i in enumerate(base['installers']):
        i.update(sha256=str(index)*64,size_bytes=1024,signature={'status':'unsigned','policy':'record-unsigned'})
        i['download_url'] = r.BASE + i['asset']
    return base


def source_manifest():
    return json.loads((ROOT.parent / 'LichAI-Desktop/release-manifests/desktop.json').read_text()) if (ROOT.parent / 'LichAI-Desktop').exists() else json.loads((ROOT / 'tests/fixtures/desktop-manifest.json').read_text())


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.policy = json.loads((ROOT / 'registry/trusted-sources.json').read_text())
        self.grant = self.policy['applications']['desktop']
        self.run = {'id':1,'run_attempt':1,'run_number':1,'status':'completed','conclusion':'success','repository':{'full_name':self.grant['repository']},
            'head_repository':{'full_name':self.grant['repository']},'path':'.github/workflows/windows-build.yml','head_branch':'main','event':'push','head_sha':'a'*40,'updated_at':'2026-10-19T09:00:00Z'}

    def test_migration_schema_and_eight_fixed_names(self):
        data = json.loads((ROOT / 'registry/applications.json').read_text())
        r.validate_registry(data)
        r.validate_policy(self.policy)
        self.assertEqual({i['asset'] for a in data['applications'] for i in a['installers']}, {
            'LichAI.Android.apk','LichAI.TV.apk','LichAI.Desktop.exe','LichAI.Desktop.msi',
            'LichAI-Excel-Translater.exe','LichAI-Word-Translator.exe','LichAI-Studio-Windows.exe','LichAI-Studio-Android.apk'})

    def test_new_app_nine_windows(self):
        app = manifest('app-nine')
        app['installers'] = [dict(app['installers'][0], asset='App.Nine.exe',download_url=r.BASE+'App.Nine.exe')]
        r.validate_registry({'schema_version':1,'applications':[app]})

    def test_app_ten_two_platforms(self):
        app = manifest('app-ten')
        app['installers'][0].update(asset='App.Ten.exe',download_url=r.BASE+'App.Ten.exe')
        app['installers'][1].update(asset='App.Ten.apk',download_url=r.BASE+'App.Ten.apk',platform='android',format='apk',signature_policy='required',signature={'status':'verified','policy':'required','certificate_sha256':'a'*64})
        r.validate_registry({'schema_version':1,'applications':[app]})

    def test_add_platform_without_changing_other_apps(self):
        before = manifest();after=copy.deepcopy(before)
        after['installers'].append(dict(after['installers'][0],platform='android',asset='New.apk',format='apk',download_url=r.BASE+'New.apk'))
        r.check_transition(before, after)
        self.assertEqual(len(before['installers']),2)

    def test_exe_msi_same_group_version(self):
        app=manifest()
        projected=r.project({'schema_version':1,'applications':[app]}, {})['app-versions.json']['windows']
        self.assertEqual(projected['latest_version'],'1.0.0')
        self.assertEqual(projected['download_url_exe'],r.BASE+'LichAI.Desktop.exe')
        self.assertEqual(projected['download_url_msi'],r.BASE+'LichAI.Desktop.msi')
        self.assertNotIn('latest_code',projected)  # Never invent build code from SemVer.

    def test_independent_android_code(self):
        app=manifest();app['legacy_key']='android';app['version_code']=18
        data=r.project({'schema_version':1,'applications':[app]}, {'product':{'name':'keep'}})
        self.assertEqual(data['app-versions.json']['android']['latest_code'],18)
        self.assertEqual(data['app-versions.json']['product']['name'],'keep')

    def test_same_version_different_hash_refused(self):
        app=manifest();other=copy.deepcopy(app);other['installers'][0]['sha256']='f'*64
        with self.assertRaisesRegex(ValueError,'Same version'):r.check_transition(app,other)

    def test_rerun_identical_bytes_is_idempotent(self):
        r.check_transition(manifest(),manifest())

    def test_downgrade_refused(self):
        app=manifest();other=manifest();other['version']='0.9.9'
        with self.assertRaises(ValueError):r.check_transition(app,other)

    def test_build_code_cannot_be_inferred_or_reused(self):
        app=manifest();app['version_code']=18
        for code in [None,17,18]:
            other=copy.deepcopy(app);other.update(version='1.0.1',version_code=code)
            with self.assertRaises(ValueError):r.check_transition(app,other)

    def test_signing_key_change_refused(self):
        app=manifest();app['installers'][0]['signature']['certificate_sha256']='a'*64
        other=copy.deepcopy(app);other['version']='1.0.1';other['installers'][0]['signature']['certificate_sha256']='b'*64
        with self.assertRaisesRegex(ValueError,'Signing key'):r.check_transition(app,other)

    def test_invalid_manifest_missing_metadata(self):
        import jsonschema
        for field in ['name','installers','version_source','source_repository']:
            m=source_manifest();m.pop(field)
            with self.assertRaises(jsonschema.ValidationError):r.validate_manifest(m,self.grant,'desktop')

    def test_manifest_cannot_steal_asset(self):
        m=source_manifest();m['installers'][0]['asset']='LichAI.Android.apk'
        with self.assertRaises(ValueError):r.validate_manifest(m,self.grant,'desktop')

    def test_policy_prevents_cross_application_collision(self):
        policy=copy.deepcopy(self.policy);policy['applications']['desktop']['assets'].append('LichAI.Android.apk')
        with self.assertRaises(ValueError):r.validate_policy(policy)

    def test_failed_fork_and_unapproved_branch_refused(self):
        for change in [{'conclusion':'failure'}, {'event':'pull_request'}, {'head_branch':'test'}, {'head_repository':{'full_name':'attacker/fork'}}]:
            with self.assertRaises(ValueError):r.validate_run(dict(self.run,**change),self.grant)

    def test_signature_cannot_be_disabled_for_apk(self):
        grant=self.policy['applications']['android']
        m=source_manifest();m.update(id='android',source_repository=grant['repository'],workflow=grant['workflows'][0],artifact=grant['artifact'],legacy_key='android')
        m['installers']=[dict(m['installers'][0],format='apk',asset='LichAI.Android.apk')]
        with self.assertRaisesRegex(ValueError,'signing'):r.validate_manifest(m,grant,'android')

    def test_archive_traversal_rejected(self):
        for path in ['../evil.exe','/evil.exe','a\\evil.exe']:
            data=io.BytesIO()
            with zipfile.ZipFile(data,'w') as z:z.writestr(path,b'bad')
            with tempfile.TemporaryDirectory() as d, self.assertRaises(ValueError):r.extract_zip(data.getvalue(),Path(d))

    def test_corrupt_build_artifact_is_not_an_installer(self):
        with tempfile.TemporaryDirectory() as d:
            file=Path(d)/'bad.exe';file.write_bytes(b'not an installer'*100)
            with self.assertRaises(ValueError):r.verify_binary(file,{'format':'exe','signature_policy':'record-unsigned'})

    def test_expired_and_deleted_artifact_refused(self):
        expiry=(datetime.now(timezone.utc)-timedelta(days=1)).isoformat()
        for artifacts in [[],[{'name':self.grant['artifact'],'expired':True}],
                          [{'name':self.grant['artifact'],'expired':False,'expires_at':expiry}]]:
            with patch.object(r,'source_file',return_value=json.dumps(source_manifest())),patch.object(r,'pages',return_value=artifacts),tempfile.TemporaryDirectory() as d:
                with self.assertRaises(ValueError):r.stage('desktop',self.grant,self.run,Path(d))

    def test_restore_detects_changed_bytes_and_missing_groups(self):
        app=manifest();assets={i['asset']:{'name':i['asset'],'state':'uploaded','size':i['size_bytes'],'digest':'sha256:'+i['sha256']} for i in app['installers']}
        with patch.object(r,'release_assets',return_value={}):self.assertIn('desktop',r.reconcile({'applications':[app]}))
        assets['LichAI.Desktop.exe']['digest']='sha256:'+'f'*64
        with patch.object(r,'release_assets',return_value=assets),self.assertRaisesRegex(ValueError,'changed public bytes'):r.reconcile({'applications':[app]})

    def test_group_publish_failure_rolls_back_and_leaves_pending(self):
        app=manifest();old=copy.deepcopy(app);old['version']='0.9.0'
        assets={i['asset']:{'name':i['asset'],'state':'uploaded','size':1,'digest':'sha256:'+'f'*64} for i in app['installers']}
        calls=[]
        with tempfile.TemporaryDirectory() as d:
            directory=Path(d);(directory/'registry').mkdir();folder=directory/'installers';folder.mkdir()
            for i in app['installers']:(folder/i['asset']).write_bytes(b'data')
            def fake_gh(*args,**kwargs):
                calls.append(args)
                if args[:2]==('release','download'):(directory/'backups'/args[6]).write_bytes(b'backup')
                return ''
            with patch.object(r,'ROOT',directory),patch.object(r,'validate_registry'),patch.object(r,'commit_state'),patch.object(r,'release_assets',return_value=assets),patch.object(r,'gh',side_effect=fake_gh),patch.object(r,'verify_group',side_effect=ValueError('upload failed')):
                with self.assertRaisesRegex(ValueError,'upload failed'):r.publish_group(app,folder,{'schema_version':1,'applications':[old]})
                self.assertTrue((directory/'registry/pending.json').exists())
                self.assertFalse((directory/'registry/applications.json').exists())
                self.assertEqual(len([c for c in calls if c[:2]==('release','upload')]),4)

    def test_studio_requires_all_ci_jobs(self):
        meta={'verified_head':'a'*40,'verified_run_id':2,'android':{'signed':True}}
        run={'head_sha':'a'*40,'conclusion':'success','path':'.github/workflows/ci.yml','id':2}
        with patch.object(r,'api',return_value=run),patch.object(r,'pages',return_value=[{'name':'windows','conclusion':'success'}]):
            with self.assertRaisesRegex(ValueError,'required CI'):r.verify_studio('nvhiepbk/LichAI-Studio',meta,{'event':'workflow_dispatch'})

    def test_studio_pr_must_be_merged(self):
        with patch.object(r,'api',return_value={'merged':False}):
            with self.assertRaisesRegex(ValueError,'approved merged'):r.verify_studio('nvhiepbk/LichAI-Studio',{'verified_head':'a'*40},{'event':'pull_request','pull_requests':[{'number':1}]})

    def test_studio_merged_pr_lookup_when_run_omits_prs(self):
        head='a'*40
        meta={'verified_head':head,'verified_run_id':2,'android':{'signed':True}}
        run={'head_sha':head,'conclusion':'success','path':'.github/workflows/ci.yml','id':2}
        pr={'merged':True,'base':{'ref':'main'},'head':{'sha':head}}
        jobs=[{'name':name,'conclusion':'success'} for name in ('validate','windows','android','android-emulator')]
        def lookup(path, key=None):
            return [{'number':8}] if '/commits/' in path else jobs
        with patch.object(r,'pages',side_effect=lookup),patch.object(r,'api',side_effect=[pr,run]):
            r.verify_studio('nvhiepbk/LichAI-Studio',meta,{'event':'pull_request','pull_requests':[]})
        pr['head']['sha']='b'*40
        with patch.object(r,'pages',side_effect=lookup),patch.object(r,'api',return_value=pr):
            with self.assertRaisesRegex(ValueError,'approved merged'):
                r.verify_studio('nvhiepbk/LichAI-Studio',meta,{'event':'pull_request','pull_requests':[]})

    def test_concurrency_is_global_and_legacy_writers_retired(self):
        workflow=(ROOT/'.github/workflows/reconcile-registry.yml').read_text()
        self.assertIn('group: lichai-public-release-writer',workflow)
        self.assertIn('cancel-in-progress: false',workflow)
        self.assertNotIn('release upload',(ROOT/'.github/workflows/restore-public-installers.yml').read_text())
        self.assertIn('uses: ./.github/workflows/reconcile-registry.yml',(ROOT/'.github/workflows/update-public-changelog.yml').read_text())

    def test_pending_transaction_can_recover_partial_replacement(self):
        app=manifest()
        with patch.object(r,'release_assets',return_value={i['asset']:{'name':i['asset'],'size':1,'digest':'sha256:'+'f'*64} for i in app['installers']}):
            self.assertEqual(r.reconcile({'applications':[app]},exclude={'desktop'}),{})

    def test_dry_run_stages_exact_artifact_without_any_release_write(self):
        m=source_manifest()
        archive=io.BytesIO()
        with zipfile.ZipFile(archive,'w') as z:
            z.writestr('bundle/LichAI.exe',b'MZ'+b'0'*1024)
            z.writestr('bundle/LichAI.msi',b'0'*1024)
        artifact={'id':9,'name':self.grant['artifact'],'expired':False,'expires_at':(datetime.now(timezone.utc)+timedelta(days=1)).isoformat()}
        def source(repo,sha,path):
            self.assertEqual(sha,self.run['head_sha'])
            return json.dumps(m) if path.endswith('desktop.json') else json.dumps({'version':'1.0.0'}) if path.endswith('tauri.conf.json') else 'Release notes'
        with patch.object(r,'source_file',side_effect=source),patch.object(r,'pages',return_value=[artifact]),patch.object(r,'gh',return_value=archive.getvalue()) as gh,patch.object(r,'verify_binary',return_value={'status':'unsigned','policy':'record-unsigned'}),tempfile.TemporaryDirectory() as d:
            new,folder=r.stage('desktop',self.grant,self.run,Path(d))
            self.assertEqual(new['provenance']['artifact_id'],9)
            self.assertEqual(len(list(folder.iterdir())),2)
            self.assertEqual(new['version'],'1.0.0')
            self.assertTrue(all(call.args[0]=='api' for call in gh.call_args_list))

    def test_full_group_success_changes_only_its_registry_entry(self):
        app=manifest();other=manifest('other')
        other['installers']=[dict(other['installers'][0],asset='Other.exe',download_url=r.BASE+'Other.exe')]
        original=copy.deepcopy(other)
        with tempfile.TemporaryDirectory() as d:
            directory=Path(d);(directory/'registry').mkdir();folder=directory/'installers';folder.mkdir()
            registry={'schema_version':1,'applications':[other]}
            with patch.object(r,'ROOT',directory),patch.object(r,'validate_registry'),patch.object(r,'commit_state'),patch.object(r,'release_assets',return_value={}),patch.object(r,'gh'),patch.object(r,'verify_group') as verify,patch.object(r,'write_projection') as project:
                r.publish_group(app,folder,registry)
            verify.assert_called_once_with(app['installers'])
            project.assert_called_once()
            self.assertEqual(registry['applications'][0],original)
            self.assertFalse((directory/'registry/pending.json').exists())

if __name__ == '__main__':unittest.main()
