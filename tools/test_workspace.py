"""Behavioral checks for the delivered project/manifest helper."""
import contextlib
import importlib.util
import io
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml

SOURCE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('workspace_cli', SOURCE / 'tools/workspace.py')
cli = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cli)


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'workspace'
        shutil.copytree(SOURCE, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def tearDown(self):
        self.temp.cleanup()

    def edit_yaml(self, relative, change):
        path = self.root / relative
        data = cli.load_yaml(path)
        change(data)
        path.write_text(yaml.safe_dump(data, sort_keys=False))

    def test_delivered_contracts_validate(self):
        self.assertEqual(cli.validate(self.root), [])

    def test_project_creation_is_valid_and_does_not_overwrite(self):
        with contextlib.redirect_stdout(io.StringIO()):
            cli.new_project(self.root, 'salon-demo', 'Salon Demo')
        manifest = cli.load_yaml(self.root / 'projects/salon-demo/project.yaml')
        self.assertEqual(manifest['id'], 'salon-demo')
        self.assertEqual(manifest['name'], 'Salon Demo')
        self.assertIsNone(manifest['repository']['path'])
        self.assertEqual(cli.validate(self.root), [])
        with self.assertRaises(ValueError):
            cli.new_project(self.root, 'salon-demo', 'Overwrite')
        self.assertEqual(cli.load_yaml(self.root / 'projects/salon-demo/project.yaml')['name'], 'Salon Demo')

    def test_slug_cannot_escape_project_folder(self):
        for slug in ['../outside', 'A B', '/tmp/project', 'salon/child']:
            with self.assertRaises(ValueError):
                cli.new_project(self.root, slug, 'Bad')

    def test_unknown_skill_is_rejected(self):
        self.edit_yaml('projects/example-project/project.yaml',
                       lambda data: data['default_skills'].append('nonexistent'))
        self.assertTrue(any('unknown default skill' in e for e in cli.validate(self.root)))

    def test_missing_document_is_rejected(self):
        (self.root / 'projects/example-project/REQUIREMENTS.md').unlink()
        self.assertTrue(any('Missing referenced file' in e for e in cli.validate(self.root)))

    def test_document_escape_is_rejected(self):
        self.edit_yaml('projects/example-project/project.yaml',
                       lambda data: data['docs'].update({'overview': '../../README.md'}))
        self.assertTrue(any('escapes its root' in e for e in cli.validate(self.root)))

    def test_invalid_source_state_is_rejected(self):
        self.edit_yaml('projects/ai-workspace/context/sources.yaml',
                       lambda data: data['sources'][0].update({'processing_status': 'approved'}))
        self.assertTrue(any('processing_status' in e for e in cli.validate(self.root)))

    def test_duplicate_source_id_is_rejected(self):
        self.edit_yaml('projects/ai-workspace/context/sources.yaml',
                       lambda data: data['sources'].append(dict(data['sources'][0])))
        self.assertTrue(any('duplicate source ID' in e for e in cli.validate(self.root)))

    def test_unknown_tool_is_rejected(self):
        self.edit_yaml('skills/context-intake/skill.yaml',
                       lambda data: data['tools'].append('unconnected-magic-tool'))
        self.assertTrue(any('unknown tool' in e for e in cli.validate(self.root)))

    def test_tampered_upstream_rule_is_rejected(self):
        path = self.root / 'skills/vercel-react-best-practices/references/upstream/rules/async-parallel.md'
        path.write_text(path.read_text() + '\nUnreviewed change.\n')
        self.assertTrue(any('checksum mismatch' in e for e in cli.validate(self.root)))

    def test_missing_laravel_rendered_rule_is_rejected(self):
        path = self.root / 'skills/laravel-best-practices/references/upstream/rules/security.md'
        path.unlink()
        self.assertTrue(any('Missing referenced file' in e for e in cli.validate(self.root)))

    def test_modified_entry_is_rejected_by_lock(self):
        path = self.root / 'skills/web-design-guidelines/SKILL.md'
        path.write_text(path.read_text() + '\nUnreviewed entry change.\n')
        self.assertTrue(any('locked entry_sha256 mismatch' in e for e in cli.validate(self.root)))

    def test_native_install_copies_complete_reviewed_entries(self):
        destination = Path(self.temp.name) / 'native'
        installed = cli.install_skills(self.root, destination)
        self.assertEqual(len(installed), 4)
        for path in installed:
            self.assertTrue((path / 'SKILL.md').is_file())
            self.assertTrue((path / 'provenance.json').is_file())
        self.assertTrue((destination / 'laravel-best-practices/references/upstream/rules/security.md').is_file())
        self.assertTrue((destination / 'web-design-guidelines/references/interface-guidelines/command.md').is_file())

    def test_install_collision_is_rejected_before_partial_copy(self):
        destination = Path(self.temp.name) / 'native'
        existing = destination / 'web-design-guidelines'
        existing.mkdir(parents=True)
        (existing / 'keep.txt').write_text('existing user content')
        with self.assertRaises(ValueError):
            cli.install_skills(self.root, destination)
        self.assertFalse((destination / 'vercel-react-best-practices').exists())
        self.assertEqual((existing / 'keep.txt').read_text(), 'existing user content')

    def test_install_subset_and_unknown_selection(self):
        destination = Path(self.temp.name) / 'native'
        with self.assertRaises(ValueError):
            cli.install_skills(self.root, destination, ['not-reviewed'])
        self.assertFalse(destination.exists())
        installed = cli.install_skills(self.root, destination, ['laravel-best-practices'])
        self.assertEqual([p.name for p in installed], ['laravel-best-practices'])


if __name__ == '__main__':
    unittest.main()
