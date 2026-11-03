import argparse
import json
from pathlib import Path

import yaml

from apidog_import.importer import import_docs, write_result

PUBLIC_MODULE_ID = 543607

parser = argparse.ArgumentParser(description='Import Apidog guides into the portal.')
parser.add_argument('export', type=Path, help='Apidog project export (JSON); keep it outside the repository')
parser.add_argument('--spec', type=Path, default=Path('docs/specs/public.openapi.yaml'))
parser.add_argument('--docs', type=Path, default=Path('docs'))
parser.add_argument('--report', type=Path, default=Path('import-report.md'))
parser.add_argument('--module', type=int, default=PUBLIC_MODULE_ID, help='Apidog module with public guides')
parser.add_argument('--languages', default='en,pl')
args = parser.parse_args()

result = import_docs(
    json.loads(args.export.read_text(encoding='utf-8')),
    yaml.safe_load(args.spec.read_text(encoding='utf-8')),
    args.module,
    languages=tuple(args.languages.split(',')),
)
write_result(result, args.docs, args.report)
print(f'{len(result.pages)} pages, {len(result.unresolved)} unresolved links, report: {args.report}')
