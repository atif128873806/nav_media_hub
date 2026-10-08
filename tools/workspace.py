#!/usr/bin/env python3
"""Validate portable workspace contracts or copy a new project template.

This tool does not execute AI, interpret sources, or run application commands.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit('Missing dependencies. In your virtual environment run: '
             'python3 -m pip install -r tools/requirements.txt')

DEFAULT_ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path):
    with path.open(encoding='utf-8') as file:
        return yaml.safe_load(file)


def contained_file(base: Path, relative: str) -> Path:
    """Resolve an existing pointer that cannot escape its declared document root."""
    if Path(relative).is_absolute():
        raise ValueError(f'Document pointer must be relative: {relative}')
    target = (base / relative).resolve()
    if not target.is_relative_to(base.resolve()):
        raise ValueError(f'Document pointer escapes its root: {relative}')
    if not target.is_file():
        raise ValueError(f'Missing referenced file: {target}')
    return target


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    def check(call):
        try:
            return call()
        except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as error:
            errors.append(str(error))
            return None

    def contract(path: Path, name: str):
        data = load_yaml(path)
        spec = json.loads((root / 'workspace/schemas' / f'{name}.schema.json').read_text())
        Draft202012Validator.check_schema(spec)
        failures = list(Draft202012Validator(spec).iter_errors(data))
        if failures:
            messages = '; '.join(f'{list(e.absolute_path)}: {e.message}' for e in failures)
            raise ValueError(f'{path}: {messages}')
        return data

    config = check(lambda: load_yaml(root / 'workspace.yaml'))
    if not isinstance(config, dict):
        errors.append('workspace.yaml must be a mapping.')
        return errors
    for target in config.get('sources_of_truth', {}).values():
        check(lambda target=target: contained_file(root, target))
    for name, target in config.get('paths', {}).items():
        if not (root / target).is_dir():
            errors.append(f'Missing workspace directory {name}: {target}')

    skill_registry = check(lambda: load_yaml(root / 'workspace/registries/skills.yaml'))
    tool_registry = check(lambda: load_yaml(root / 'workspace/registries/tools.yaml'))
    if not isinstance(skill_registry, dict) or not isinstance(tool_registry, dict):
        errors.append('Skill/tool registries must be mappings.')
        return errors
    skill_ids = skill_registry.get('skills', [])
    if not isinstance(skill_ids, list) or any(not isinstance(x, str) for x in skill_ids):
        errors.append('Skill registry must contain a list of string IDs.')
        return errors
    if len(skill_ids) != len(set(skill_ids)):
        errors.append('Duplicate skill IDs in registry.')
    tool_ids = set(tool_registry.get('tools', {}))
    manifests = {p.parent.name: p for p in (root / 'skills').glob('*/skill.yaml')}
    if set(manifests) != set(skill_ids):
        errors.append('Skill registry and actual manifests differ.')

    for skill_id in skill_ids:
        data = check(lambda: contract(root / 'skills' / skill_id / 'skill.yaml', 'skill'))
        if data is None:
            continue
        if data['id'] != skill_id:
            errors.append(f'Skill folder/manifest ID mismatch: {skill_id}')
        for companion in data['recommended_with']:
            if companion not in skill_ids:
                errors.append(f'{skill_id}: unknown companion {companion}')
        for tool in data['tools']:
            if tool not in tool_ids:
                errors.append(f'{skill_id}: unknown tool {tool}')
        instructions = check(lambda: contained_file(root / 'skills' / skill_id, data['instructions']))
        if instructions:
            text = instructions.read_text(encoding='utf-8')
            front = re.match(r'^---\n(.*?)\n---\n', text, re.S)
            if not front:
                errors.append(f'{skill_id}: missing SKILL.md frontmatter')
            else:
                metadata = check(lambda: yaml.safe_load(front.group(1)))
                if not isinstance(metadata, dict) or metadata.get('name') != skill_id or not metadata.get('description'):
                    errors.append(f'{skill_id}: invalid SKILL.md name/description')

        if data.get('provenance'):
            provenance_path = check(lambda: contained_file(root / 'skills' / skill_id, data['provenance']))
            if provenance_path:
                def inspect_provenance():
                    provenance = json.loads(provenance_path.read_text(encoding='utf-8'))
                    if provenance.get('id') != skill_id:
                        raise ValueError(f'{skill_id}: provenance ID mismatch')
                    records = provenance.get('files')
                    if not isinstance(records, list) or not records:
                        raise ValueError(f'{skill_id}: missing provenance records')
                    paths = set()
                    for record in records:
                        relative = record['path']
                        if relative in paths:
                            raise ValueError(f'{skill_id}: duplicate provenance path {relative}')
                        paths.add(relative)
                        file = contained_file(provenance_path.parent, relative)
                        checksum = hashlib.sha256(file.read_bytes()).hexdigest()
                        if checksum != record['sha256']:
                            raise ValueError(f'{skill_id}: checksum mismatch for {relative}')
                        if not re.fullmatch(r'[0-9a-f]{40}', record['revision']):
                            raise ValueError(f'{skill_id}: invalid source revision')
                    source_entry = provenance_path.parent / 'references/upstream/SOURCE_SKILL.md'
                    text = source_entry.read_text(encoding='utf-8')
                    # Laravel's official index links rules rendered by Boost. Ensure the
                    # shipped portable companions are actually present, rather than
                    # publishing an index with missing Blade-derived Markdown rules.
                    for link in re.findall(r'\]\((rules/[^)]+\.md)\)', text):
                        contained_file(source_entry.parent, link)
                check(inspect_provenance)

    lock = check(lambda: load_yaml(root / 'workspace/upstream-lock.yaml')) if (root / 'workspace/upstream-lock.yaml').exists() else None
    if lock is not None:
        def inspect_lock():
            locked_ids = set()
            for item in lock['skills']:
                skill_id = item['id']
                if skill_id in locked_ids or skill_id not in skill_ids:
                    raise ValueError(f'Invalid/duplicate upstream lock ID: {skill_id}')
                locked_ids.add(skill_id)
                for key, path in [('entry_sha256', f'skills/{skill_id}/SKILL.md'),
                                  ('provenance_sha256', item['provenance'])]:
                    file = contained_file(root, path)
                    if hashlib.sha256(file.read_bytes()).hexdigest() != item[key]:
                        raise ValueError(f'{skill_id}: locked {key} mismatch')
                provenance = json.loads(contained_file(root, item['provenance']).read_text())
                if provenance['revision'] != item['revision'] or provenance['repository'] != item['repository']:
                    raise ValueError(f'{skill_id}: lock and provenance source differ')
            declared = {skill_id for skill_id, path in manifests.items() if load_yaml(path).get('provenance')}
            if declared != locked_ids:
                raise ValueError('Upstream lock and imported skill manifests differ.')
        check(inspect_lock)

    project_paths = sorted((root / 'projects').glob('*/project.yaml'))
    if not project_paths:
        errors.append('No project manifests found.')
    for path in project_paths:
        data = check(lambda path=path: contract(path, 'project'))
        if data is None:
            continue
        if data['id'] != path.parent.name:
            errors.append(f'{path}: project ID must match folder name')
        for skill_id in data['default_skills']:
            if skill_id not in skill_ids:
                errors.append(f'{path}: unknown default skill {skill_id}')
        for tool in data['tools']:
            if tool not in tool_ids:
                errors.append(f'{path}: unknown tool {tool}')
        for pointer in data['docs'].values():
            check(lambda pointer=pointer: contained_file(path.parent, pointer))
        registry = check(lambda: contract(path.parent / data['docs']['sources'], 'sources'))
        if registry is None:
            continue
        ids = set()
        for source in registry['sources']:
            if source['id'] in ids:
                errors.append(f'{path}: duplicate source ID {source["id"]}')
            ids.add(source['id'])
            if source.get('path'):
                source_root = (path.parent / data['docs']['sources']).parent
                check(lambda source=source: contained_file(source_root, source['path']))
            if source['type'] == 'website' and not source.get('url'):
                errors.append(f'{path}: website source {source["id"]} needs URL')
    return errors


def install_skills(root: Path, destination: Path, selected: list[str] | None = None) -> list[Path]:
    """Copy reviewed native entries without network access or overwriting existing names."""
    errors = validate(root)
    if errors:
        raise ValueError('Workspace validation failed before installation: ' + '; '.join(errors))
    lock = load_yaml(root / 'workspace/upstream-lock.yaml')
    available = [item['id'] for item in lock['skills']]
    requested = available if not selected else list(dict.fromkeys(selected))
    for skill_id in requested:
        if skill_id not in available:
            raise ValueError(f'Not a reviewed imported skill: {skill_id}')
    destination = destination.expanduser().resolve()
    targets = [destination / skill_id for skill_id in requested]
    for target in targets:
        if target.exists() or target.is_symlink():
            raise ValueError(f'Existing skill; nothing overwritten: {target}')
    # Preflight all destinations so a later collision never leaves a partial install.
    destination.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    try:
        for skill_id, target in zip(requested, targets):
            if target.exists() or target.is_symlink():
                raise ValueError(f'Destination changed during installation: {target}')
            # Track a newly allocated directory before copytree, allowing a failed copy
            # to remove only the directory this invocation created.
            target.mkdir()
            created.append(target)
            shutil.copytree(root / 'skills' / skill_id, target, dirs_exist_ok=True)
    except Exception:
        for target in reversed(created):
            shutil.rmtree(target)
        raise
    return created


def new_project(root: Path, slug: str, name: str):
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', slug):
        raise ValueError('Use a lowercase project slug containing letters, digits, or hyphens.')
    target = root / 'projects' / slug
    if target.exists():
        raise ValueError(f'Project already exists; nothing overwritten: {target}')
    template = root / 'projects/example-project'
    if not (template / 'project.yaml').is_file():
        raise ValueError('Missing example-project template.')
    # Copy only the project template. No repository, source extraction, or commands run.
    shutil.copytree(template, target)
    data = load_yaml(target / 'project.yaml')
    data['id'], data['name'] = slug, name
    data['repository']['path'] = None
    (target / 'project.yaml').write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    overview = target / 'PROJECT.md'
    content = overview.read_text(encoding='utf-8')
    overview.write_text('# ' + name + '\n' + content.split('\n', 1)[1], encoding='utf-8')
    print(f'Created {target}. Configure actual repository, scope, sources, and checks before work.')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=DEFAULT_ROOT)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('validate', help='Check schemas, IDs, registries, and document/source paths.')
    create = commands.add_parser('new-project', help='Copy the project template without overwriting.')
    create.add_argument('slug')
    create.add_argument('--name', required=True)
    install = commands.add_parser('install-skills', help='Copy reviewed upstream entries into an explicit native skill directory.')
    install.add_argument('--destination', type=Path, required=True)
    install.add_argument('--skill', action='append', dest='selected')
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == 'new-project':
            new_project(root, args.slug, args.name)
            return 0
        if args.command == 'install-skills':
            for target in install_skills(root, args.destination, args.selected):
                print(f'Copied {target}. Verify skill discovery in your coding tool.')
            return 0
        errors = validate(root)
        if errors:
            for error in errors:
                print(f'ERROR: {error}', file=sys.stderr)
            return 1
        print('PASS: workspace contracts, skill/project manifests, registries, and source/document pointers.')
        print('This checks structure only; it does not verify application behavior, approval, or AI compliance.')
        return 0
    except (ValueError, KeyError, OSError, yaml.YAMLError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
