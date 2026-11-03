import json
import tempfile
import unittest
from pathlib import Path

from openapi_json import on_post_build, spec_to_json

SPEC = """openapi: 3.0.3
info:
  title: Fixture
  version: 1.0.0
paths:
  /v1/order:
    post:
      responses:
        200:
          description: OK
          content:
            application/json:
              example:
                invoiceDate: 2026-04-17
                createdAt: 2026-04-17T10:00:00+02:00
                meta: {}
                country: NO
                cod: yes
                active: true
"""


class SpecToJsonTest(unittest.TestCase):
    def setUp(self):
        self.spec = json.loads(spec_to_json(SPEC))
        self.example = self.spec['paths']['/v1/order']['post']['responses']['200']['content']['application/json']['example']

    def test_keeps_dates_as_iso_strings(self):
        self.assertEqual('2026-04-17', self.example['invoiceDate'])
        self.assertEqual('2026-04-17T10:00:00+02:00', self.example['createdAt'])

    def test_reads_yes_no_as_strings_like_yaml_1_2(self):
        self.assertEqual('NO', self.example['country'])
        self.assertEqual('yes', self.example['cod'])
        self.assertIs(True, self.example['active'])

    def test_keeps_empty_object_and_string_status_codes(self):
        self.assertEqual({}, self.example['meta'])
        self.assertIn('200', self.spec['paths']['/v1/order']['post']['responses'])


class PostBuildTest(unittest.TestCase):
    def test_writes_json_next_to_every_yaml_spec(self):
        with tempfile.TemporaryDirectory() as root:
            docs, site = Path(root, 'docs'), Path(root, 'site')
            (docs / 'specs').mkdir(parents=True)
            (docs / 'specs' / 'public.openapi.yaml').write_text(SPEC, encoding='utf-8')

            on_post_build({'docs_dir': str(docs), 'site_dir': str(site)})

            written = json.loads((site / 'specs' / 'public.openapi.json').read_text(encoding='utf-8'))
            self.assertEqual('3.0.3', written['openapi'])


if __name__ == '__main__':
    unittest.main()
