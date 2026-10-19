"""Release protocol v1: trusted manifest -> exact successful run -> verified group.
No event payload, source repository script, or artifact is executed by this tool.
"""
from __future__ import annotations
import argparse
import base64
import copy
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = 'nvhiepbk/LichAI-Public'
TAG = 'LichAI-Public'
BASE = f'https://github.com/{PUBLIC}/releases/download/{TAG}/'


def gh(*args, binary=False):
    return subprocess.check_output(['gh', *map(str, args)], text=not binary)


def api(path):
    return json.loads(gh('api', path))


def pages(path, key=None):
    result = []
    for page in range(1, 101):
        data = api(path + ('&' if '?' in path else '?') + f'per_page=100&page={page}')
        batch = data[key] if key else data
        result.extend(batch)
        if len(batch) < 100:
            return result
    raise ValueError('API pagination limit reached; refusing incomplete results')


def source_file(repo, sha, path):
    data = api(f'repos/{repo}/contents/{path}?ref={sha}')
    return base64.b64decode(data['content']).decode('utf-8-sig')


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def semver(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d+\.\d+\.\d+', value):
        raise ValueError(f'Invalid stable version: {value!r}')
    return tuple(map(int, value.split('.')))


def validate_manifest(data, grant, aid):
    import jsonschema
    jsonschema.validate(data, json.loads((ROOT / 'registry/manifest.schema.json').read_text()))
    if (data['id'] != aid or data['source_repository'] != grant['repository']
            or data['workflow'] not in grant['workflows'] or data['artifact'] != grant['artifact']
            or data.get('legacy_key') != grant.get('legacy_key')):
        raise ValueError('Manifest identity does not match reviewed trust policy')
    names = [x['asset'] for x in data['installers']]
    if len(names) != len(set(names)) or set(names) != set(grant['assets']):
        raise ValueError('Manifest must match the entire approved installer group')
    for item in data['installers']:
        if item['format'] == 'apk' and item['signature_policy'] != 'required':
            raise ValueError('APK signing is mandatory')
    return data


def validate_policy(policy):
    assets, legacy = set(), set()
    for aid, grant in policy['applications'].items():
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', aid):
            raise ValueError('Unsafe application id')
        if not re.fullmatch(r'nvhiepbk/[A-Za-z0-9_.-]+', grant['repository']):
            raise ValueError('Repository must be explicitly approved')
        for name in grant['assets']:
            if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]+\.(apk|exe|msi|dmg|pkg|deb|rpm|AppImage|zip)', name) or name in assets:
                raise ValueError('Unsafe or overlapping asset ownership')
            assets.add(name)
        key = grant.get('legacy_key')
        if key:
            if key in legacy:
                raise ValueError('Duplicate legacy metadata owner')
            legacy.add(key)


def validate_run(run, grant):
    if (run.get('status') != 'completed' or run.get('conclusion') != 'success'
            or run['repository']['full_name'] != grant['repository']
            or run.get('head_repository', {}).get('full_name') != grant['repository']
            or run['path'].split('@')[0].split('/')[-1] not in grant['workflows']):
        raise ValueError('Untrusted or unsuccessful workflow run')
    if grant.get('studio_approval'):
        if run['event'] not in ('pull_request', 'workflow_dispatch') or (run['event'] == 'workflow_dispatch' and run['head_branch'] != 'main'):
            raise ValueError('Studio publication requires merged/main or explicit main dispatch')
    elif run['head_branch'] != 'main' or run['event'] not in ('push', 'workflow_dispatch'):
        raise ValueError('Only stable main builds may publish')
    if not re.fullmatch(r'[0-9a-f]{40}', run['head_sha']):
        raise ValueError('Invalid immutable source SHA')


def extract_zip(raw, directory):
    """Extract data only, reject traversal, links, oversized archives and duplicate names."""
    seen = set()
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        if sum(x.file_size for x in archive.infolist()) > 2 * 1024**3:
            raise ValueError('Artifact too large')
        for item in archive.infolist():
            path = Path(item.filename)
            if (path.is_absolute() or '..' in path.parts or '\\' in item.filename
                    or item.filename in seen or (item.external_attr >> 16) & 0o170000 == 0o120000):
                raise ValueError('Unsafe artifact path')
            seen.add(item.filename)
        archive.extractall(directory)


def hash_file(path):
    with path.open('rb') as file:
        return hashlib.file_digest(file, 'sha256').hexdigest()


def verify_binary(path, item):
    """Verify format and signatures without launching downloaded software."""
    fmt = item['format']
    header = path.read_bytes()[:8]
    if path.stat().st_size < 128:
        raise ValueError('Empty/truncated installer')
    signature = {'status': 'unsigned', 'policy': item['signature_policy']}
    if fmt == 'apk':
        with zipfile.ZipFile(path) as archive:
            if 'AndroidManifest.xml' not in archive.namelist() or archive.testzip():
                raise ValueError('Invalid APK')
        signer = os.environ.get('APKSIGNER', 'apksigner')
        result = subprocess.check_output([signer, 'verify', '--verbose', '--print-certs', str(path)], text=True)
        cert = re.search(r'Signer #1 certificate SHA-256 digest:\s*([0-9a-fA-F]{64})', result)
        if not cert:
            raise ValueError('Missing verified signing certificate')
        signature.update(status='verified', certificate_sha256=cert[1].lower())
    elif fmt == 'exe':
        import pefile
        if not header.startswith(b'MZ'):
            raise ValueError('Invalid PE installer')
        pe = pefile.PE(str(path), fast_load=True)
        if not pe.sections or any(section.PointerToRawData + section.SizeOfRawData > path.stat().st_size for section in pe.sections):
            raise ValueError('Truncated PE sections')
        pe.close()
    elif fmt == 'msi':
        import olefile
        if header != bytes.fromhex('d0cf11e0a1b11ae1') or not olefile.isOleFile(path):
            raise ValueError('Invalid MSI installer')
        with olefile.OleFileIO(path) as ole:
            if not ole.listdir():
                raise ValueError('Empty MSI database')
    elif fmt == 'zip':
        with zipfile.ZipFile(path) as archive:
            if not archive.namelist() or archive.testzip():
                raise ValueError('Invalid ZIP bundle')
    elif fmt == 'deb' and header != b'!<arch>\n':
        raise ValueError('Invalid Debian package')
    elif fmt == 'rpm' and not header.startswith(bytes.fromhex('edabeedb')):
        raise ValueError('Invalid RPM package')
    elif fmt == 'pkg' and not header.startswith(b'xar!'):
        raise ValueError('Invalid macOS package')
    elif fmt == 'dmg':
        with path.open('rb') as file:
            file.seek(-512, 2)
            if file.read(4) != b'koly':
                raise ValueError('Invalid UDIF disk image')
    elif fmt == 'AppImage':
        with path.open('rb') as file:
            ident = file.read(12)
        if not ident.startswith(b'\x7fELF') or ident[8:10] != b'AI':
            raise ValueError('Invalid AppImage')
    elif fmt not in ('exe', 'msi', 'apk', 'zip', 'deb', 'rpm', 'pkg', 'dmg', 'AppImage'):
        raise ValueError('Unsupported installer format')
    if item['signature_policy'] == 'required' and signature['status'] != 'verified':
        raise ValueError('Required signature verifier unavailable')
    return signature


def read_version(manifest, run, folder):
    src = manifest['version_source']
    text = (folder / src['path']).read_text(encoding='utf-8-sig') if src['kind'] == 'studio' else source_file(manifest['source_repository'], run['head_sha'], src['path'])
    code = None
    if src['kind'] == 'gradle':
        version = re.search(r'versionName\s*=\s*"(?:TV )?([^"]+)"', text)[1]
        code = int(re.search(r'versionCode\s*=\s*(\d+)', text)[1])
    elif src['kind'] == 'tauri':
        version = json.loads(text)['version']
    elif src['kind'] == 'studio':
        meta = json.loads(text)
        version = meta['version']
        verify_studio(manifest['source_repository'], meta, run)
    else:
        version = text.strip()
    semver(version)
    return version, code


def verify_studio(repo, publication, publication_run):
    """Approval is a merged PR for the tested source, or a main-only manual publication run.
    The enclosing publication run is checked separately. Recheck all four CI jobs.
    """
    if publication_run['event'] == 'pull_request':
        approved = False
        for candidate in publication_run.get('pull_requests', []):
            pr = api(f'repos/{repo}/pulls/{int(candidate["number"])}')
            if pr.get('merged') and pr['base']['ref'] == 'main' and pr['head']['sha'] == publication['verified_head']:
                approved = True
        if not approved:
            raise ValueError('Studio publication is not tied to an approved merged source PR')
    head = publication['verified_head']
    if not re.fullmatch('[0-9a-f]{40}', head):
        raise ValueError('Invalid verified Studio source')
    run = api(f'repos/{repo}/actions/runs/{int(publication["verified_run_id"])}')
    if run['head_sha'] != head or run['conclusion'] != 'success' or run['path'] != '.github/workflows/ci.yml':
        raise ValueError('Studio evidence does not refer to the tested source')
    jobs = pages(f'repos/{repo}/actions/runs/{run["id"]}/jobs', 'jobs')
    passed = {j['name'] for j in jobs if j['conclusion'] == 'success'}
    if not {'validate', 'windows', 'android', 'android-emulator'} <= passed:
        raise ValueError('Studio required CI jobs have not all passed')
    if not publication.get('android', {}).get('signed'):
        raise ValueError('Unsigned Studio candidate')


def check_transition(old, new):
    if not old:
        return
    if semver(new['version']) < semver(old['version']):
        raise ValueError('Refusing version downgrade from migration seed')
    if old.get('release_status') != 'published':
        return
    before, after = semver(old['version']), semver(new['version'])
    if after < before:
        raise ValueError('Refusing version downgrade')
    if old.get('version_code') is not None:
        if new.get('version_code') is None or new['version_code'] < old['version_code']:
            raise ValueError('Refusing independent build-code downgrade')
        if after > before and new['version_code'] <= old['version_code']:
            raise ValueError('A new APK version requires an increased versionCode')
    old_assets = {i['asset']: i for i in old['installers']}
    for item in new['installers']:
        prior = old_assets.get(item['asset'])
        if not prior:
            continue
        cert = prior.get('signature', {}).get('certificate_sha256')
        if cert and cert != item.get('signature', {}).get('certificate_sha256'):
            raise ValueError('Signing key rotation requires reviewed migration')
        if after == before and prior['sha256'] != item['sha256']:
            raise ValueError('Same version has different bytes: increment version before publishing')


def validate_registry(registry):
    import jsonschema
    jsonschema.validate(registry, json.loads((ROOT / 'registry/registry.schema.json').read_text()))
    ids, assets = set(), set()
    for app in registry['applications']:
        if app['id'] in ids:
            raise ValueError('Duplicate application id')
        ids.add(app['id'])
        for item in app['installers']:
            if item['asset'] in assets:
                raise ValueError('Duplicate installer ownership')
            assets.add(item['asset'])


def release_assets():
    release = api(f'repos/{PUBLIC}/releases/tags/{TAG}')
    if release['draft'] or release['prerelease']:
        raise ValueError('Shared release must be stable and public')
    return {x['name']: x for x in pages(f'repos/{PUBLIC}/releases/{release["id"]}/assets')}


def matches(asset, item):
    return bool(asset and asset.get('state') == 'uploaded' and asset['size'] == item['size_bytes']
                and asset.get('digest') == 'sha256:' + item['sha256'])


def verify_group(items):
    assets = release_assets()
    for item in items:
        if not matches(assets.get(item['asset']), item):
            raise ValueError('Public asset size/digest mismatch: ' + item['asset'])


def stage(aid, grant, run, directory):
    validate_run(run, grant)
    manifest = validate_manifest(json.loads(source_file(grant['repository'], run['head_sha'], grant['manifest_path'])), grant, aid)
    artifacts = pages(f'repos/{grant["repository"]}/actions/runs/{run["id"]}/artifacts', 'artifacts')
    candidates = [a for a in artifacts if a['name'] == grant['artifact'] and not a['expired']]
    if len(candidates) != 1:
        raise ValueError('Need exactly one unexpired artifact from the exact run')
    artifact = candidates[0]
    if datetime.fromisoformat(artifact['expires_at'].replace('Z', '+00:00')) <= datetime.now(timezone.utc):
        raise ValueError('Artifact has expired')
    raw = gh('api', f'repos/{grant["repository"]}/actions/artifacts/{artifact["id"]}/zip', binary=True)
    expected = artifact.get('digest')
    if expected and expected != 'sha256:' + hashlib.sha256(raw).hexdigest():
        raise ValueError('Artifact digest mismatch')
    unpacked = directory / 'artifact'
    extract_zip(raw, unpacked)
    version, code = read_version(manifest, run, unpacked)
    result = copy.deepcopy(manifest)
    result.update(version=version, version_code=code, release_status='published', published_at=run['updated_at'][:10],
                  provenance={'run_id': run['id'], 'run_attempt': run['run_attempt'], 'head_sha': run['head_sha'],
                              'artifact_id': artifact['id'], 'workflow': run['path']},
                  changes=source_file(grant['repository'], run['head_sha'], manifest['changelog_path']).splitlines())
    files = directory / 'installers'
    files.mkdir()
    for item in result['installers']:
        found = [p for p in unpacked.rglob(item['pattern']) if p.is_file()]
        if len(found) != 1:
            raise ValueError('Missing or ambiguous installer: ' + item['asset'])
        target = files / item['asset']
        shutil.copyfile(found[0], target)
        item.update(size_bytes=target.stat().st_size, sha256=hash_file(target), download_url=BASE + item['asset'],
                    signature=verify_binary(target, item))
        if item['format'] == 'apk':
            badging = subprocess.check_output([os.environ.get('AAPT', 'aapt'), 'dump', 'badging', str(target)], text=True)
            package = re.search(r"package:.*versionCode='(\d+)'.*versionName='([^']+)'", badging)
            if not package or package[2].removeprefix('TV ') != version or (code is not None and int(package[1]) != code):
                raise ValueError('APK embedded version differs from source metadata')
            if code is None:
                result['version_code'] = int(package[1])
        if grant.get('studio_approval'):
            meta = json.loads((unpacked / 'publication.json').read_text())
            original = meta[item['platform']]
            if original['sha256'] != item['sha256'] or original['version'] != version:
                raise ValueError('Studio approved package hash/version mismatch')
            if item['format'] == 'apk' and original.get('signing_certificate_sha256') != item['signature'].get('certificate_sha256'):
                raise ValueError('Studio signing certificate mismatch')
            result['verified_head'] = meta['verified_head']
    return result, files


def project(registry, legacy):
    """Keep existing update clients, Studio SEO and Translator metadata compatible."""
    result = {'app-versions.json': copy.deepcopy(legacy)}
    for app in registry['applications']:
        if app['release_status'] != 'published':
            continue
        key = app.get('legacy_key')
        if key:
            data = result['app-versions.json'].setdefault(key, {})
            data.update(latest_version=app['version'], release_date=app['published_at'], changes=app['changes'])
            if app.get('version_code') is not None:
                data['latest_code'] = app['version_code']
            elif key == 'windows':
                data.pop('latest_code', None)  # Desktop compares SemVer; it has no independent build code.
            for item in app['installers']:
                suffix = '_' + item['format'] if len(app['installers']) > 1 else ''
                data['download_url' + suffix] = item['download_url']
        metadata = {}
        for item in app['installers']:
            m = dict(item, version=app['version'], release_status='published', published_at=app['published_at'],
                     verified_head=app.get('verified_head', app['provenance']['head_sha']),
                     signed=item['signature']['status'] == 'verified',
                     signing_certificate_sha256=item['signature'].get('certificate_sha256'),
                     info_url=app['info_url'], guide_url=app['guide_url'])
            metadata[item['platform']] = m
        if app['id'] == 'studio':
            result['studio-release.json'] = dict(id='studio', name=app['name'], schema_version=1, version=app['version'],
                published_at=app['published_at'], verified_head=app['verified_head'], info_url=app['info_url'], guide_url=app['guide_url'], **metadata)
        if app['id'] in ('excel-translator', 'word-translator'):
            filename = 'translator-version.json' if app['id'] == 'excel-translator' else 'word-translator-version.json'
            result[filename] = next(iter(metadata.values()))
    result['application-registry.json'] = registry
    return result


def write_projection(registry):
    legacy = json.loads((ROOT / 'registry/legacy-app-versions.json').read_text())
    for name, data in project(registry, legacy).items():
        dump(ROOT / 'metadata' / name, data)
    studio = ROOT / 'metadata/studio-release.json'
    if studio.exists():
        shutil.copyfile(studio, ROOT / 'apps/studio.json')
    text = '# Application release catalogue\n\n'
    for app in registry['applications']:
        if app['release_status'] == 'published':
            text += f'## {app["name"]} {app["version"]} · {app["published_at"]}\n\n' + '\n'.join(app['changes']) + '\n\n'
    (ROOT / 'RELEASE-CATALOG.md').write_text(text, encoding='utf-8')
    for app in registry['applications']:
        if app['release_status'] == 'published':
            (ROOT / 'release-notes' / (app['id'] + '.md')).write_text(
                f'## {app["name"]} {app["version"]} · {app["published_at"]}\n\n' + '\n'.join(app['changes']) + '\n', encoding='utf-8')
    changelog = ROOT / 'CHANGELOG.md'
    original = changelog.read_text(encoding='utf-8').split('<!-- registry:start -->')[0].rstrip()
    changelog.write_text(original + '\n\n<!-- registry:start -->\n' + text + '<!-- registry:end -->\n', encoding='utf-8')


def commit_state(message):
    # Global workflow concurrency serializes ALL release and restore writers.
    subprocess.run(['git', 'add', 'registry', 'metadata', 'apps/studio.json', 'RELEASE-CATALOG.md', 'release-notes', 'CHANGELOG.md'], cwd=ROOT, check=True)
    if subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=ROOT).returncode:
        subprocess.run(['git', 'commit', '-m', message], cwd=ROOT, check=True)
        subprocess.run(['git', 'push', 'origin', 'HEAD:main'], cwd=ROOT, check=True)


def publish_group(new, folder, registry):
    old = next((a for a in registry['applications'] if a['id'] == new['id']), None)
    check_transition(old, new)
    # Persist intended hashes BEFORE replacing any stable URL. A crash resumes this exact
    # source run on the next scheduled/manual run; it never searches for a different build.
    prospective = copy.deepcopy(registry)
    prospective['applications'] = [a for a in registry['applications'] if a['id'] != new['id']] + [new]
    validate_registry(prospective)
    dump(ROOT / 'registry/pending.json', {'application': new, 'run_id': new['provenance']['run_id']})
    commit_state('Record pending verified release transaction ' + new['id'])
    assets = release_assets()
    backups = folder.parent / 'backups'
    backups.mkdir(exist_ok=True)
    changed = []
    try:
        for item in new['installers']:
            name = item['asset']
            if matches(assets.get(name), item):
                continue
            if name in assets:
                gh('release', 'download', TAG, '-R', PUBLIC, '-p', name, '-D', backups)
            changed.append(name)
            gh('release', 'upload', TAG, '-R', PUBLIC, '--clobber', folder / name)
        verify_group(new['installers'])
        registry['applications'] = [a for a in registry['applications'] if a['id'] != new['id']] + [new]
        dump(ROOT / 'registry/applications.json', registry)
        write_projection(registry)
        (ROOT / 'registry/pending.json').unlink()
        commit_state('Publish verified release catalogue ' + new['id'] + ' ' + new['version'])
    except Exception:
        # Revert changed URLs if possible; durable pending state remains for exact-run retry.
        for name in reversed(changed):
            if (backups / name).exists():
                gh('release', 'upload', TAG, '-R', PUBLIC, '--clobber', backups / name)
            elif name not in assets:
                gh('release', 'delete-asset', TAG, name, '-R', PUBLIC, '--yes')
        raise


def reconcile(registry, exclude=()):
    assets = release_assets()
    missing, mismatch = [], []
    for app in registry['applications']:
        if app['release_status'] != 'published' or app['id'] in exclude:
            continue
        for item in app['installers']:
            if item['asset'] not in assets:
                missing.append(app)
            elif not matches(assets[item['asset']], item):
                mismatch.append(item['asset'])
    if mismatch:
        raise ValueError('Unexpected changed public bytes; manual investigation required: ' + ', '.join(mismatch))
    return {app['id']: app for app in missing}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--audit', action='store_true')
    args = parser.parse_args()
    policy = json.loads((ROOT / 'registry/trusted-sources.json').read_text())
    validate_policy(policy)
    registry = json.loads((ROOT / 'registry/applications.json').read_text())
    validate_registry(registry)
    plan, errors = [], []
    pending_path = ROOT / 'registry/pending.json'
    pending = json.loads(pending_path.read_text()) if pending_path.exists() else None
    repairs = reconcile(registry, exclude={pending['application']['id']} if pending else set())
    if args.audit:
        if repairs or pending:
            raise ValueError('Missing assets or incomplete transaction; run reconcile in apply mode')
        print('All registered public assets match exact SHA-256 and size')
        return
    for aid, grant in policy['applications'].items():
        try:
            old = next((a for a in registry['applications'] if a['id'] == aid), None)
            if pending and pending['application']['id'] != aid:
                continue  # Recover an interrupted transaction before accepting new releases.
            if pending:
                run = api(f'repos/{grant["repository"]}/actions/runs/{pending["run_id"]}')
            elif aid in repairs:
                run = api(f'repos/{grant["repository"]}/actions/runs/{old["provenance"]["run_id"]}')
            else:
                runs = []
                for workflow in grant['workflows']:
                    branch_filter = '' if grant.get('studio_approval') else 'branch=main&'
                    runs.extend(api(f'repos/{grant["repository"]}/actions/workflows/{workflow}/runs?{branch_filter}status=success&per_page=30')['workflow_runs'])
                qualified = []
                for candidate in runs:
                    try:
                        validate_run(candidate, grant)
                    except ValueError:
                        continue
                    # A successful Studio CI without publication artifact is not an approval.
                    if grant.get('studio_approval'):
                        available = pages(f'repos/{grant["repository"]}/actions/runs/{candidate["id"]}/artifacts', 'artifacts')
                        if not any(a['name'] == grant['artifact'] for a in available):
                            continue
                    qualified.append(candidate)
                runs = qualified
                if not runs:
                    continue
                run = max(runs, key=lambda r: r['run_number']) if len(grant['workflows']) == 1 else max(runs, key=lambda r: r['created_at'])
                if old and old.get('provenance', {}).get('run_id') == run['id']:
                    continue
            with tempfile.TemporaryDirectory() as directory:
                new, folder = stage(aid, grant, run, Path(directory))
                check_transition(old, new)
                if pending:
                    expected = {i['asset']: i['sha256'] for i in pending['application']['installers']}
                    if expected != {i['asset']: i['sha256'] for i in new['installers']}:
                        raise ValueError('Pending transaction bytes no longer match exact run')
                plan.append({'id': aid, 'version': new['version'], 'run_id': run['id'], 'installers': new['installers']})
                if args.apply:
                    publish_group(new, folder, registry)
        except Exception as exc:
            errors.append({'id': aid, 'error': str(exc)})
            if pending_path.exists() or args.apply:
                break
    dump(ROOT / 'release-report.json', {'apply': args.apply, 'plan': plan, 'errors': errors})
    print(json.dumps({'plan': plan, 'errors': errors}, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)
    if args.apply:
        # Notes are derived from committed verified metadata and are safe to retry independently.
        gh('release', 'edit', TAG, '-R', PUBLIC, '--notes-file', ROOT / 'RELEASE-CATALOG.md')


if __name__ == '__main__':
    main()
