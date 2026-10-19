import copy
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from release_registry import keep_catalogue_page_links

class ProductPageLinksTests(unittest.TestCase):
    def test_reviewed_page_survives_generic_source_default(self):
        old={'id':'android','info_url':'https://lich.ai.vn/lich-ai-android','guide_url':'https://lich.ai.vn/lich-ai-android#huong-dan'}
        new={'id':'android','info_url':'https://lich.ai.vn/download','guide_url':'https://lich.ai.vn/download','version':'2.0.0','installers':[{'sha256':'a'*64}]}
        original=copy.deepcopy(new)
        keep_catalogue_page_links(old,new)
        self.assertEqual(new['info_url'],old['info_url']);self.assertEqual(new['guide_url'],old['guide_url'])
        self.assertEqual(new['version'],original['version']);self.assertEqual(new['installers'],original['installers'])
    def test_explicit_new_page_not_overwritten(self):
        new={'id':'android','info_url':'https://lich.ai.vn/new-page','guide_url':'https://lich.ai.vn/new-guide'}
        original=copy.deepcopy(new)
        keep_catalogue_page_links({'id':'android','info_url':'https://lich.ai.vn/old-page'},new)
        self.assertEqual(new,original)
    def test_unknown_or_other_owner_not_copied(self):
        for prior in ['https://lich.ai.vn.evil.test/page','javascript:bad','https://example.com/page',None]:
            new={'id':'android','info_url':'https://lich.ai.vn/download'}
            keep_catalogue_page_links({'id':'tv','info_url':prior},new)
            self.assertEqual(new['info_url'],'https://lich.ai.vn/download')
        new={'id':'android','info_url':'https://lich.ai.vn/download'}
        keep_catalogue_page_links({'id':'android','info_url':'https://lich.ai.vn.evil.test/page'},new)
        self.assertEqual(new['info_url'],'https://lich.ai.vn/download')
