# developer.globkurier.pl

Public GlobKurier developer portal: integration guides, API reference (Swagger UI) and API changelog.
Served at <https://developer.globkurier.pl/> (GitHub Pages).

This repository holds **documentation only**: markdown and the public OpenAPI spec. API behaviour lives in
[globkurier.pl](https://github.com/velesan/globkurier.pl), which is the source of truth for the spec.

> The repository is public. Never commit internal documentation, `admin.openapi.yaml`, Apidog exports,
> ticket numbers, real tokens or personal data.

## Run locally

Python 3.10+:

```bash
python3 -m venv .venv          # Ubuntu without python3-venv: pip install --user virtualenv && python3 -m virtualenv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
```

Open <http://localhost:8000> (Polish: `/pl/`, German: `/de/`).

## Layout

| Path | Content |
|---|---|
| `mkdocs.yml` | left menu (`nav`), languages and their menu titles (`nav_translations`) |
| `docs/<lang>/` | pages per language: `en` (default), `pl`, `de`; same file names in every language |
| `docs/<lang>/guides/` | integration guides (imported from Apidog) |
| `docs/<lang>/api/<name>.md` | one page per API, rendered with Swagger UI (`template: api.html`, `spec: specs/<file>`) |
| `docs/specs/` | OpenAPI specs, copied from gk; **do not edit here** |
| `docs/assets/swagger-ui/` | Swagger UI 4.38.7, same build as gk `/v1/docs` (`globkurier.pl/docs/api/swagger-ui/`) |
| `overrides/api.html` | Swagger UI page, same config as gk `SwaggerUiPage`, plus download links (JSON / YAML) |
| `hooks/openapi_json.py` | publishes every `docs/specs/*.yaml` also as `.json` at build time |
| `tools/apidog_import/` | one-off Apidog importer, see its [README](tools/apidog_import/README.md) |

## Adding content

- **Page**: add `docs/en/<path>.md` (+ `pl`, `de` with the same path), add it to `nav` in `mkdocs.yml`,
  add its menu title to `nav_translations` of `pl` and `de`. A missing translation falls back to English.
- **Link to an endpoint**: `[Create order](api/globkurier.md#/Orders/orderCreate)` — `#/<tag>/<operationId>` from the spec,
  spaces in the tag as `%20`.
- **API**: put the spec in `docs/specs/`, add `docs/<lang>/api/<name>.md` with `template: api.html` and `spec:`, add it under
  `API reference` in `nav`.
- **API changelog**: publish a GitHub Release (tag e.g. `api-2026-11-03`, notes in English). The changelog page loads
  releases in the browser (`docs/assets/releases.js`), so no portal rebuild is needed; pre-releases are hidden.
  Describe contract changes only (endpoints, fields, statuses), no ticket numbers or internal names.

## Spec updates

`docs/specs/public.openapi.yaml` is a copy of `globkurier.pl/docs/api/public.openapi.yaml` at the latest production tag
(`prod-*`), so the portal documents what is deployed. Updates arrive as pull requests from the gk release workflow;
it must open them with a GitHub App or PAT token, because pull requests created with `GITHUB_TOKEN` do not trigger CI here.
Manual sync (`GK_DIR` = your gk checkout):

```bash
GK_DIR=../globkurier
git -C "$GK_DIR" fetch --tags
TAG=$(git -C "$GK_DIR" tag -l 'prod-*' --sort=-creatordate | head -1)
git -C "$GK_DIR" show "$TAG:docs/api/public.openapi.yaml" > docs/specs/public.openapi.yaml
```

## Checks (CI and locally)

```bash
(cd tools && ../.venv/bin/python -m unittest discover -s apidog_import/tests -t .)
(cd hooks && ../.venv/bin/python -m unittest)
node --test tests/
npx --yes @redocly/cli@1.25.5 lint --config redocly.yaml docs/specs/public.openapi.yaml
.venv/bin/mkdocs build --strict
```

`build --strict` fails on a broken link or a `nav` entry without a page. CI also fails on any `apidog://` link left in `docs/`.
Pushes to `main` deploy to GitHub Pages.
