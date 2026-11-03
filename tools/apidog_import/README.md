# Importing documentation from Apidog

One-off migration of the Apidog guides (project 844225) into `docs/<lang>/guides/`.
Endpoints are **not** imported: the API reference comes from the gk spec (`docs/specs/public.openapi.yaml`).

## 1. Export from Apidog

Apidog → project settings → *Export* → format **Apidog** (`.apidog.json`), whole project.
Keep the file **outside this repository** (`*apidog*.json` is git-ignored and CI fails on a committed export): it contains internal modules
(admin business analysis, internal endpoints) that must never be published.

## 2. Run the importer

From the repository root, with the `.venv` from the main README:

```bash
PYTHONPATH=tools .venv/bin/python -m apidog_import /path/to/GlobKurier.apidog.json
```

Options: `--module` (Apidog module with public guides, default `543607`), `--languages` (default `en,pl`),
`--spec`, `--docs`, `--report`.

What it does:

| Apidog | Portal |
|---|---|
| page `Labels (PL)` / `Labels (EN)` | `docs/pl/guides/labels.md` / `docs/en/guides/labels.md` |
| page without `(XX)` suffix | copied to every language (listed in the report) |
| `apidog://link/endpoint/<id>` | Swagger deep link `../api/globkurier.md#/<tag>/<operationId>`, matched by method + path (path parameter names ignored) |
| `apidog://link/pages/<id>` | link to the page in the same language |
| `<Container>`, `<DataSchema …/>` | removed (the container keeps its content) |
| other modules (e.g. internal `858641`) | skipped |

A link that cannot be resolved (endpoint missing in the gk spec, unknown id) becomes plain text and is listed
in `import-report.md` — no dead links.

## 3. Review before committing

1. Read `import-report.md`: unresolved links, missing languages, removed components.
2. Check examples for real data (e-mails, phone numbers, tax IDs) — the repository is public.
   The first import (2026-11-03) replaced `ala@o2.pl` → `odbiorca@example.com`, NIP `2532451081` → `1234563218`,
   VAT `PL2220872890` → `PL1234563218` (valid checksum, fictitious); a re-import brings the originals back.
3. Re-importing overwrites `docs/en|pl/guides/*.md`; manual edits and `docs/de/` translations of those pages must be redone.
4. Run the checks from the main README (`build --strict` must pass) and open a PR.

After the migration Apidog is no longer the source: edit the markdown in this repository.
