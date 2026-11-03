"""MkDocs hook: publishes every docs/specs/*.yaml also as JSON, so the spec can be downloaded in both formats."""
import json
import re
from pathlib import Path

import yaml


class _Yaml12Loader(yaml.SafeLoader):
    """PyYAML follows YAML 1.1: unquoted NO/yes/on become booleans and dates become date objects.

    OpenAPI tools read YAML 1.2, where only true/false are booleans; the country code NO must stay a string.
    """


_Yaml12Loader.yaml_implicit_resolvers = {
    first: [(tag, regexp) for tag, regexp in resolvers if tag not in ('tag:yaml.org,2002:bool', 'tag:yaml.org,2002:timestamp')]
    for first, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
_Yaml12Loader.add_implicit_resolver('tag:yaml.org,2002:bool', re.compile(r'^(?:true|True|TRUE|false|False|FALSE)$'), list('tTfF'))


def spec_to_json(yaml_text):
    return json.dumps(yaml.load(yaml_text, Loader=_Yaml12Loader), ensure_ascii=False, indent=2)


def on_post_build(config, **kwargs):
    site_specs = Path(config['site_dir'], 'specs')
    site_specs.mkdir(parents=True, exist_ok=True)
    for spec in Path(config['docs_dir'], 'specs').glob('*.yaml'):
        (site_specs / f'{spec.stem}.json').write_text(spec_to_json(spec.read_text(encoding='utf-8')), encoding='utf-8')
