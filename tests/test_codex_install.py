import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
INSTALLER = REPO_ROOT / "tools" / "install_codex.py"
spec = importlib.util.spec_from_file_location("install_codex", INSTALLER)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class CodexInstallationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="boji codex ")
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.destination = self.directory / "project" / ".agents" / "skills"

    def test_complete_suite_and_local_resources_are_installed(self):
        installed = installer.install_skills(self.destination)
        plugin = json.loads(
            (REPO_ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            {path.name for path in installed},
            {command["name"] for command in plugin["commands"]},
        )
        for skill in installed:
            manifest = (skill / "SKILL.md").read_text(encoding="utf-8")
            self.assertRegex(manifest, rf"(?m)^name: {re.escape(skill.name)}$")
            for target in re.findall(r"\]\((\./[^)]+)\)", manifest):
                self.assertTrue((skill / target).is_file(), (skill.name, target))

    def test_cli_accepts_destination_and_unrelated_working_directory(self):
        result = subprocess.run(
            [sys.executable, str(INSTALLER), "--dest", str(self.destination)],
            cwd=self.directory,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Installed 14 skills", result.stdout)
        self.assertTrue((self.destination / "boji" / "SKILL.md").is_file())

    def test_default_destination_belongs_to_the_installer_repository(self):
        checkout = self.directory / "checkout"
        (checkout / "tools").mkdir(parents=True)
        shutil.copy2(INSTALLER, checkout / "tools" / INSTALLER.name)
        shutil.copytree(REPO_ROOT / "skills", checkout / "skills")
        subprocess.run(
            [sys.executable, str(checkout / "tools" / INSTALLER.name)],
            cwd=self.directory,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertTrue((checkout / ".agents/skills/boji/SKILL.md").is_file())
        self.assertFalse((self.directory / ".agents").exists())

    def test_existing_installation_is_not_overwritten_or_partially_updated(self):
        previous = self.destination / "boji-workout"
        previous.mkdir(parents=True)
        sentinel = previous / "SKILL.md"
        sentinel.write_text("my customization", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            installer.install_skills(self.destination)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "my customization")
        self.assertEqual(list(self.destination.iterdir()), [previous])

    def test_broken_destination_symlink_is_not_replaced(self):
        self.destination.mkdir(parents=True)
        link = self.destination / "boji"
        try:
            link.symlink_to(self.directory / "missing", target_is_directory=True)
        except (OSError, NotImplementedError) as error:
            self.skipTest(f"Symlinks unavailable: {error}")
        with self.assertRaises(FileExistsError):
            installer.install_skills(self.destination)
        self.assertTrue(link.is_symlink())

    def test_destination_inside_source_is_rejected(self):
        with self.assertRaises(ValueError):
            installer.install_skills(REPO_ROOT / "skills" / "nested")

    def test_installed_calculator_works_without_the_checkout(self):
        checkout = self.directory / "removed checkout"
        shutil.copytree(REPO_ROOT / "skills", checkout / "skills")
        with mock.patch.object(installer, "REPO_ROOT", checkout):
            installer.install_skills(self.destination)
        shutil.rmtree(checkout)
        arguments = ["--height", "175", "--weight", "75", "--pullups", "3"]
        installed_script = (
            self.destination / "boji-diagnosis" / "scripts" / "calc_metrics.py"
        )
        installed = subprocess.run(
            [sys.executable, str(installed_script), *arguments],
            cwd=self.directory,
            capture_output=True,
            text=True,
            check=True,
        )
        original_cli = subprocess.run(
            [sys.executable, str(REPO_ROOT / "tools/calc_metrics.py"), *arguments],
            cwd=self.directory,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(installed.stdout, original_cli.stdout)
        self.assertIn("BMR): 1724 kcal/天", installed.stdout)
        self.assertIn("TDEE): 2370 kcal/天", installed.stdout)


if __name__ == "__main__":
    unittest.main()
