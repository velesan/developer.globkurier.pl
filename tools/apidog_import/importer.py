"""Converts an Apidog project export into portal guides.

Endpoints are not migrated: the portal renders the GlobKurier spec, so links to Apidog endpoints are
resolved to Swagger UI deep links of the matching spec operation (method + path).
"""
import re
import unicodedata
from dataclasses import dataclass, field
from urllib.parse import quote

import yaml

API_PAGE = '../api/globkurier.md'
HTTP_METHODS = {'get', 'post', 'put', 'patch', 'delete'}
LANGUAGE_SUFFIX = re.compile(r'^(?P<title>.+?)\s*\((?P<lang>[A-Z]{2})\)$')
APIDOG_LINK = re.compile(r'\[(?P<text>[^\]]*)\]\((?P<target>apidog://link/(?P<kind>endpoint|pages)/(?P<id>\d+))\)')
LEFTOVER_APIDOG_LINK = re.compile(r'apidog://[^\s)"\'>\]]+')
PATH_PARAM = re.compile(r'\{[^}]+\}')
# Apidog-only MDX components; outside Apidog they render as unknown HTML, so they are dropped (wrappers keep their content).
APIDOG_COMPONENT = re.compile(r'</?Container>|<DataSchema\b[^>]*/>')


@dataclass(frozen=True)
class Page:
    lang: str
    slug: str
    title: str
    content: str


@dataclass(frozen=True)
class UnresolvedLink:
    page: str
    target: str
    reason: str


@dataclass
class ImportResult:
    pages: list = field(default_factory=list)
    unresolved: list = field(default_factory=list)
    notes: list = field(default_factory=list)


@dataclass(frozen=True)
class _Doc:
    id: int
    slug: str
    title: str
    lang: str | None
    content: str


def import_docs(export, spec, module_id, languages):
    endpoints = _apidog_endpoints(export)
    operations = _spec_operations(spec)
    docs = [_parse_doc(item) for item in _module_docs(export, module_id)]
    docs_by_id = {doc.id: doc for doc in docs}
    result = ImportResult()

    targets = []
    for slug in dict.fromkeys(doc.slug for doc in docs):
        versions = [doc for doc in docs if doc.slug == slug]
        if all(doc.lang is None for doc in versions):
            result.notes.append(f'{slug}: no language suffix, copied to every language')
            targets += [(lang, versions[0]) for lang in languages]
        else:
            targets += [(doc.lang, doc) for doc in versions if doc.lang in languages]
            missing = [lang for lang in languages if lang not in {doc.lang for doc in versions}]
            if missing:
                result.notes.append(f'{slug}: missing {", ".join(missing)}')

    available = {(lang, doc.slug) for lang, doc in targets}
    for lang, doc in targets:
        page_id = f'{lang}/{doc.slug}'
        resolve = lambda match: _resolve_link(match, lang, page_id, endpoints, operations, docs_by_id, available, result)
        content = APIDOG_LINK.sub(resolve, _strip_components(doc.content, page_id, result))
        for target in dict.fromkeys(LEFTOVER_APIDOG_LINK.findall(content)):
            result.unresolved.append(UnresolvedLink(page_id, target, 'unsupported link form'))
        result.pages.append(Page(lang, doc.slug, doc.title, content))

    return result


def write_result(result, docs_dir, report_path):
    for page in result.pages:
        path = docs_dir / page.lang / 'guides' / f'{page.slug}.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        front_matter = yaml.safe_dump({'title': page.title}, allow_unicode=True)
        path.write_text(f'---\n{front_matter}---\n\n{page.content.strip()}\n', encoding='utf-8')

    lines = ['# Apidog import report', '', '## Unresolved links', '', '| Page | Link | Reason |', '|---|---|---|']
    lines += [f'| {u.page} | `{u.target}` | {u.reason} |' for u in result.unresolved]
    lines += ['', '## Notes', ''] + [f'- {note}' for note in result.notes]
    report_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def _resolve_link(match, lang, page_id, endpoints, operations, docs_by_id, available, result):
    text, target, kind, item_id = match.group('text', 'target', 'kind', 'id')
    if kind == 'pages':
        doc = docs_by_id.get(int(item_id))
        if doc is None:
            reason = 'page id not in export module'
        elif (lang, doc.slug) in available:
            return f'[{text}]({doc.slug}.md)'
        else:
            reason = f'page not available in {lang}'
    elif item_id not in endpoints:
        reason = 'endpoint id not in export'
    else:
        method, path = endpoints[item_id]
        operation = operations.get((method, _normalize_path(path)))
        if operation is not None:
            tag, operation_id = operation
            return f'[{text}]({API_PAGE}#/{quote(tag, safe="")}/{quote(operation_id, safe="")})'
        reason = f'endpoint {method.upper()} {path} not in spec'

    # A dead link would look valid to readers; plain text plus a report entry keeps the fix visible.
    result.unresolved.append(UnresolvedLink(page_id, target, reason))

    return text


def _strip_components(content, page_id, result):
    for component in dict.fromkeys(APIDOG_COMPONENT.findall(content)):
        if component.startswith('<DataSchema'):
            result.notes.append(f'{page_id}: removed Apidog component {component}')

    return APIDOG_COMPONENT.sub('', content)


def _module_docs(export, module_id):
    def walk(node):
        yield from node.get('items', [])
        for child in node.get('children', []):
            yield from walk(child)

    for module in export.get('docCollection', []):
        if module.get('moduleId') == module_id:
            yield from walk(module)


def _apidog_endpoints(export):
    endpoints = {}

    def walk(node):
        for item in node.get('items', []):
            if 'api' in item:
                endpoints[str(item['api']['id'])] = (item['api']['method'].lower(), item['api']['path'])
            walk(item)
        for child in node.get('children', []):
            walk(child)

    for module in export.get('apiCollection', []):
        walk(module)

    return endpoints


def _spec_operations(spec):
    # Without an operationId Swagger UI has no deep link; untagged operations are listed under "default".
    return {
        (method, _normalize_path(path)): ((operation.get('tags') or ['default'])[0], operation['operationId'])
        for path, item in spec.get('paths', {}).items()
        for method, operation in item.items()
        if method in HTTP_METHODS and operation.get('operationId')
    }


def _normalize_path(path):
    return PATH_PARAM.sub('{}', path.rstrip('/'))


def _parse_doc(item):
    name = item['name'].strip()
    match = LANGUAGE_SUFFIX.match(name)
    title, lang = (match.group('title'), match.group('lang').lower()) if match else (name, None)

    return _Doc(item['id'], _slugify(title), title, lang, item.get('content') or '')


def _slugify(text):
    ascii_text = unicodedata.normalize('NFKD', text.replace('ł', 'l').replace('Ł', 'L')).encode('ascii', 'ignore').decode()

    return re.sub(r'[^a-z0-9]+', '-', ascii_text.lower()).strip('-')
