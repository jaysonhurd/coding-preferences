"""Exercise the local-checkout installer without network or user-home writes."""

import re
import subprocess
import tempfile
import unittest
from pathlib import Path


INSTALLER = Path(__file__).resolve().parents[1] / 'install.sh'


class InstallerTests(unittest.TestCase):
    def run_installer(self, target, *options):
        return subprocess.run(
            ['bash', str(INSTALLER), *options, str(target)], capture_output=True, text=True
        )

    def test_fresh_install_and_repeat_preserve_edits(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            result = self.run_installer(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            skill = target / '.agents/skills/agent-help/SKILL.md'
            self.assertTrue(skill.is_file())
            self.assertTrue((skill.parent / '../../docs/development-preferences.md').resolve().is_file())
            self.assertEqual({entry.name for entry in target.iterdir()}, {'.agents', 'AGENTS.md'})
            self.assertTrue((target / 'AGENTS.md').is_file())
            self.assertFalse((target / '.specify').exists())
            skill.write_text('local skill edit')
            (target / 'AGENTS.md').write_text('local instructions')
            result = self.run_installer(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(skill.read_text(), 'local skill edit')
            self.assertEqual((target / 'AGENTS.md').read_text(), 'local instructions')

    def test_installed_pointer_indexes_every_bundle_file(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            result = self.run_installer(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            bundle = target / '.agents/coding-preferences'
            guide = bundle / '.agents/FILES.md'
            self.assertIn(f'({guide.relative_to(target)})', (target / 'AGENTS.md').read_text())
            # Every shipped file has a task-specific route in the project root.
            routes = re.findall(r'`(\.agents/[^`]+)`', (target / 'AGENTS.md').read_text())
            routed_files = {(target / route).resolve() for route in routes if (target / route).is_file()}
            self.assertEqual(routed_files, {path for path in bundle.rglob('*') if path.is_file()})
            for skill_file in (bundle / 'skills').rglob('*'):
                if skill_file.is_file():
                    self.assertIn(f'.agents/{skill_file.relative_to(bundle)}', routes)
            links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', guide.read_text())
            self.assertEqual(
                {(guide.parent / link).resolve() for link in links},
                {path for path in bundle.rglob('*') if path.is_file()},
            )
            for entry in (target / '.agents/skills').iterdir():
                self.assertEqual(entry.resolve(), bundle / 'skills' / entry.name)
                self.assertIn(entry.name, guide.read_text())

    def test_default_fills_gaps_in_existing_bundle(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            bundle = target / '.agents/coding-preferences'
            bundle.mkdir(parents=True)
            (bundle / 'README.md').write_text('Existing bundle instructions')
            result = self.run_installer(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((bundle / '.agents/FILES.md').is_file())
            self.assertIn('(.agents/coding-preferences/.agents/FILES.md)', (target / 'AGENTS.md').read_text())
            self.assertEqual((bundle / 'README.md').read_text(), 'Existing bundle instructions')

    def test_overwrite_refreshes_files_root_and_skill_links(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'project'
            self.assertEqual(self.run_installer(target).returncode, 0)
            bundle = target / '.agents/coding-preferences'
            outside = Path(directory) / 'outside'
            outside.write_text('external edit')
            (target / 'AGENTS.md').unlink()
            (target / 'AGENTS.md').symlink_to(outside)
            skill_link = target / '.agents/skills/initialize-go'
            skill_link.unlink()
            skill_link.symlink_to(outside.parent, target_is_directory=True)
            (bundle / 'README.md').write_text('local edit')
            (bundle / 'LICENSE').unlink()
            (bundle / 'custom.md').write_text('project-owned')
            result = self.run_installer(target, '--overwrite')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('Installed project task map', (target / 'AGENTS.md').read_text())
            self.assertEqual(outside.read_text(), 'external edit')
            self.assertEqual(skill_link.resolve(), bundle / 'skills/initialize-go')
            for name in ['README.md', 'LICENSE']:
                self.assertEqual((bundle / name).read_bytes(), (INSTALLER.parent / name).read_bytes())
            self.assertEqual((bundle / 'custom.md').read_text(), 'project-owned')

    def test_overwrite_rejects_nested_directory_link_before_refresh(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'project'
            bundle = target / '.agents/coding-preferences'
            bundle.mkdir(parents=True)
            (bundle / 'README.md').write_text('local')
            (bundle / 'templates').symlink_to(Path(directory), target_is_directory=True)
            result = self.run_installer(target, '--overwrite')
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual((bundle / 'README.md').read_text(), 'local')
            self.assertFalse((Path(directory) / 'go-project').exists())

    def test_existing_project_files_and_broken_links_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            files = ['AGENTS.md', '.specify/memory/constitution.md',
                     '.agents/skills/speckit-plan/SKILL.md',
                     '.agents/skills/spec-kit/SKILL.md',
                     '.agent-local/config.toml', 'specs/feature/plan.md']
            for name in files:
                path = target / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('custom ' + name)
            broken = target / '.agents/skills/agent-help'
            broken.symlink_to('missing')
            result = self.run_installer(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            for name in files:
                self.assertEqual((target / name).read_text(), 'custom ' + name)
            self.assertEqual(broken.readlink(), Path('missing'))

    def test_symlink_destinations_rejected_before_writing(self):
        for name in ['.agents', '.agents/skills', '.agents/coding-preferences']:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                target = Path(directory) / 'project'
                outside = Path(directory) / 'outside'
                target.mkdir()
                outside.mkdir()
                destination = target / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.symlink_to(outside, target_is_directory=True)
                result = self.run_installer(target)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(list(outside.iterdir()), [])
                self.assertFalse((target / 'AGENTS.md').exists())

    def test_missing_nested_target_is_created(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'missing parent' / 'new project'
            result = self.run_installer(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((target / 'AGENTS.md').is_file())
            self.assertTrue((target / '.agents/skills/agent-help/SKILL.md').is_file())

    def test_file_target_fails_without_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'file'
            target.write_text('preserve me')
            result = self.run_installer(target)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(target.read_text(), 'preserve me')
