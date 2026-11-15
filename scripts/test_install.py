"""Exercise the local-checkout installer without network or user-home writes."""

import subprocess
import tempfile
import unittest
from pathlib import Path


INSTALLER = Path(__file__).resolve().parents[1] / 'install.sh'


class InstallerTests(unittest.TestCase):
    def run_installer(self, target):
        return subprocess.run(
            ['bash', str(INSTALLER), str(target)], capture_output=True, text=True
        )

    def test_fresh_install_and_repeat_preserve_edits(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            result = self.run_installer(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            skill = target / '.agents/skills/agent-help/SKILL.md'
            self.assertTrue(skill.is_file())
            self.assertTrue((skill.parent / '../../docs/development-preferences.md').resolve().is_file())
            self.assertFalse((target / '.codex').exists())
            self.assertTrue((target / 'AGENTS.md').is_file())
            self.assertFalse((target / '.specify').exists())
            skill.write_text('local skill edit')
            (target / 'AGENTS.md').write_text('local instructions')
            result = self.run_installer(target)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(skill.read_text(), 'local skill edit')
            self.assertEqual((target / 'AGENTS.md').read_text(), 'local instructions')

    def test_existing_project_files_and_broken_links_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            files = ['AGENTS.md', '.specify/memory/constitution.md',
                     '.agents/skills/speckit-plan/SKILL.md',
                     '.agents/skills/spec-kit/SKILL.md',
                     '.codex/config.toml', 'specs/feature/plan.md']
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
            self.assertFalse((target / '.agents/skills/codex-help').exists())

    def test_file_target_fails_without_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'file'
            target.write_text('preserve me')
            result = self.run_installer(target)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(target.read_text(), 'preserve me')
