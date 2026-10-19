"""Accumulate GitHub counters by asset ID; replacement never discards a period."""
import copy
from datetime import datetime, timezone
import json

REPOSITORY = 'nvhiepbk/LichAI-Public'
TAG = 'LichAI-Public'


def accumulate(ledger, assets, registry):
    if ledger.get('schema_version') != 1 or not isinstance(ledger.get('assets'), list):
        raise ValueError('Invalid download count ledger')
    owners = {}
    for app in registry['applications']:
        for item in app['installers']:
            if item['asset'] in owners:
                raise ValueError('Duplicate download count owner')
            owners[item['asset']] = app['id']
    result = copy.deepcopy(ledger)
    entries = {}
    for item in result['assets']:
        if (type(item.get('asset_id')) is not int or item['asset_id'] <= 0
                or type(item.get('download_count')) is not int or item['download_count'] < 0
                or item['asset_id'] in entries or not isinstance(item.get('name'), str)):
            raise ValueError('Invalid or duplicate asset counter')
        entries[item['asset_id']] = item
    active = set()
    for asset in assets:
        if asset['name'] not in owners:
            continue
        aid, count = asset['id'], asset['download_count']
        if type(aid) is not int or aid <= 0 or type(count) is not int or count < 0:
            raise ValueError('Invalid GitHub download counter')
        if aid in active:
            raise ValueError('Duplicate live asset ID')
        active.add(aid)
        prior = entries.get(aid)
        if prior and prior['name'] != asset['name']:
            raise ValueError('Asset renamed; review counter ownership before continuing')
        entries[aid] = {'asset_id': aid, 'name': asset['name'],
                        'download_count': max(count, prior['download_count'] if prior else 0)}
    result['assets'] = sorted(entries.values(), key=lambda a: a['asset_id'])
    totals = {app['id']: {'historical': 0, 'current': 0, 'total': 0} for app in registry['applications']}
    installers = {name: {'historical': 0, 'current': 0, 'total': 0} for name in owners}
    for item in result['assets']:
        owner = owners.get(item['name'])
        if owner:
            period = 'current' if item['asset_id'] in active else 'historical'
            totals[owner][period] += item['download_count']
            totals[owner]['total'] += item['download_count']
            installers[item['name']][period] += item['download_count']
            installers[item['name']]['total'] += item['download_count']
    return result, {'schema_version': 1, 'repository': REPOSITORY, 'release_tag': TAG, 'applications': totals, 'installers': installers}


def record(root, assets, registry):
    ledger_path = root / 'registry/download-counts.json'
    ledger = json.loads(ledger_path.read_text(encoding='utf-8'))
    ledger, summary = accumulate(ledger, assets, registry)
    snapshot_path = root / 'metadata/download-counts.json'
    if snapshot_path.exists():
        previous = json.loads(snapshot_path.read_text(encoding='utf-8'))
        if {k: v for k, v in previous.items() if k != 'updated_at'} == summary:
            summary['updated_at'] = previous.get('updated_at')
    if not summary.get('updated_at'):
        summary['updated_at'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    for path, data in ((ledger_path, ledger), (snapshot_path, summary)):
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
