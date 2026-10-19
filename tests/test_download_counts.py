import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from download_counts import accumulate, record

REGISTRY = {'applications': [
    {'id': 'desktop', 'installers': [{'asset': 'app.exe'}, {'asset': 'app.msi'}]},
    {'id': 'phone', 'installers': [{'asset': 'phone.apk'}]}]}


def asset(aid, name, count):
    return {'id': aid, 'name': name, 'download_count': count}


class DownloadCountsTests(unittest.TestCase):
    def test_replacement_and_repeat_keep_old_plus_new_once(self):
        ledger = {'schema_version': 1, 'assets': []}
        ledger, _ = accumulate(ledger, [asset(1, 'app.exe', 25), asset(2, 'app.msi', 10)], REGISTRY)
        current = [asset(3, 'app.exe', 7), asset(2, 'app.msi', 12), asset(4, 'phone.apk', 3)]
        ledger, stats = accumulate(ledger, current, REGISTRY)
        self.assertEqual(stats['applications']['desktop'], {'historical': 25, 'current': 19, 'total': 44})
        again, repeated = accumulate(ledger, current, REGISTRY)
        self.assertEqual(again, ledger)
        self.assertEqual(repeated, stats)
        _, stale = accumulate(ledger, [asset(3, 'app.exe', 1), asset(2, 'app.msi', 1)], REGISTRY)
        self.assertEqual(stale['applications']['desktop']['total'], 44)

    def test_unknown_asset_not_counted_and_duplicate_id_rejected(self):
        empty = {'schema_version': 1, 'assets': []}
        _, stats = accumulate(empty, [asset(9, 'unrelated.zip', 999)], REGISTRY)
        self.assertEqual(stats['applications']['desktop']['total'], 0)
        with self.assertRaisesRegex(ValueError, 'Duplicate live'):
            accumulate(empty, [asset(1, 'app.exe', 1), asset(1, 'app.exe', 1)], REGISTRY)
        with self.assertRaises(ValueError):
            accumulate(empty, [asset(1, 'app.exe', True)], REGISTRY)

    def test_record_keeps_timestamp_when_counts_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'registry').mkdir(); (root / 'metadata').mkdir()
            (root / 'registry/download-counts.json').write_text(json.dumps({'schema_version': 1, 'assets': []}))
            record(root, [asset(1, 'app.exe', 4)], REGISTRY)
            before = (root / 'metadata/download-counts.json').read_bytes()
            record(root, [asset(1, 'app.exe', 4)], REGISTRY)
            self.assertEqual(before, (root / 'metadata/download-counts.json').read_bytes())
