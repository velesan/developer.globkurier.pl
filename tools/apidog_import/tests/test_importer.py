import json
import tempfile
from collections import namedtuple
import unittest
from pathlib import Path

import yaml

from apidog_import.importer import import_docs, write_result

FIXTURES = Path(__file__).parent / 'fixtures'
PUBLIC_MODULE = 1
UnresolvedLinkReason = namedtuple('UnresolvedLinkReason', 'page target reason')


def load_fixtures():
    export = json.loads((FIXTURES / 'export.json').read_text(encoding='utf-8'))
    spec = yaml.safe_load((FIXTURES / 'spec.yaml').read_text(encoding='utf-8'))

    return export, spec


class ImportDocsTest(unittest.TestCase):
    def setUp(self):
        export, spec = load_fixtures()
        self.result = import_docs(export, spec, PUBLIC_MODULE, languages=('en', 'pl'))

    def page(self, lang, slug):
        return next(p for p in self.result.pages if p.lang == lang and p.slug == slug)

    def test_exports_each_doc_to_page_by_language_suffix(self):
        self.assertEqual('Labels', self.page('pl', 'labels').title)
        self.assertEqual('Labels', self.page('en', 'labels').title)

    def test_rewrites_endpoint_link_to_swagger_deep_link_by_method_and_path(self):
        self.assertIn('[Get labels](../api/globkurier.md#/Order%20Documents/getOrderLabels)', self.page('en', 'labels').content)

    def test_matches_path_params_regardless_of_name(self):
        self.assertNotIn('apidog://', self.page('pl', 'labels').content)

    def test_rewrites_page_link_to_portal_page_in_same_language(self):
        self.assertIn('[Tracking (PL)](tracking.md)', self.page('pl', 'labels').content)

    def test_reports_endpoint_missing_in_spec_and_keeps_plain_text(self):
        content = self.page('pl', 'tracking').content
        self.assertIn('Śledzenie: Removed endpoint i Unknown.', content)
        reasons = {(u.page, u.target): u.reason for u in self.result.unresolved}
        self.assertEqual('endpoint GET /v1/legacy not in spec', reasons[('pl/tracking', 'apidog://link/endpoint/103')])
        self.assertEqual('endpoint id not in export', reasons[('pl/tracking', 'apidog://link/endpoint/999')])

    def test_reports_page_link_to_page_missing_in_this_language(self):
        self.assertIn('Customs: Order with customs (PL).', self.page('en', 'labels').content)
        self.assertIn(UnresolvedLinkReason('en/labels', 'apidog://link/pages/204', 'page not available in en'), self.reasons())

    def test_reports_unsupported_apidog_link_form(self):
        self.assertIn(UnresolvedLinkReason('pl/tracking', 'apidog://link/schemas/5', 'unsupported link form'), self.reasons())

    def test_ignores_spec_operation_without_operation_id(self):
        self.assertEqual(['en'], [p.lang for p in self.result.pages if p.slug == 'tracking-statuses'])

    def reasons(self):
        return [UnresolvedLinkReason(u.page, u.target, u.reason) for u in self.result.unresolved]

    def test_skips_internal_module(self):
        self.assertFalse(any('INTERNAL' in p.content for p in self.result.pages))

    def test_reports_doc_missing_in_some_language(self):
        self.assertEqual(['pl'], [p.lang for p in self.result.pages if p.slug == 'order-with-customs'])
        self.assertIn('order-with-customs: missing en', self.result.notes)

    def test_strips_apidog_components_and_keeps_their_content(self):
        content = self.page('pl', 'order-with-customs').content
        self.assertNotIn('<Container>', content)
        self.assertNotIn('<DataSchema', content)
        self.assertIn('```mermaid\ngraph TD\n```', content)
        self.assertIn('pl/order-with-customs: removed Apidog component <DataSchema id="6874954" />', self.result.notes)

    def test_doc_without_language_suffix_goes_to_every_language(self):
        langs = sorted(p.lang for p in self.result.pages if p.slug == 'przyklady-examples-crossborder')
        self.assertEqual(['en', 'pl'], langs)
        self.assertIn('przyklady-examples-crossborder: no language suffix, copied to every language', self.result.notes)


class WriteResultTest(unittest.TestCase):
    def test_writes_guides_with_title_front_matter_and_report(self):
        export, spec = load_fixtures()
        result = import_docs(export, spec, PUBLIC_MODULE, languages=('en', 'pl'))
        with tempfile.TemporaryDirectory() as out:
            write_result(result, Path(out), Path(out) / 'import-report.md')

            page = (Path(out) / 'pl' / 'guides' / 'labels.md').read_text(encoding='utf-8')
            self.assertTrue(page.startswith('---\ntitle: Labels\n---\n\n'))
            front_matter = (Path(out) / 'en' / 'guides' / 'tracking-statuses.md').read_text(encoding='utf-8').split('---')[1]
            self.assertEqual({'title': 'Tracking: statuses'}, yaml.safe_load(front_matter))
            report = (Path(out) / 'import-report.md').read_text(encoding='utf-8')
            self.assertIn('| pl/tracking | `apidog://link/endpoint/103` | endpoint GET /v1/legacy not in spec |', report)


if __name__ == '__main__':
    unittest.main()
