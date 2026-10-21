"""Prüft CLI-Verhalten einschließlich des tatsächlichen Modulaufrufs."""

import io
import subprocess
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from importlib.metadata import version

from codex_starter.cli import main


class CliTests(unittest.TestCase):
    def test_default_greeting(self):
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main([])
        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue(), "Hallo, Welt!\n")

    def test_custom_name(self):
        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(["--name", " Andreas "])
        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue(), "Hallo, Andreas!\n")

    def test_empty_name_is_usage_error(self):
        output, errors = io.StringIO(), io.StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            with self.assertRaises(SystemExit) as raised:
                main(["--name", "  "])
        self.assertEqual(raised.exception.code, 2)
        self.assertEqual(output.getvalue(), "")
        self.assertIn("nicht leer", errors.getvalue())

    def test_missing_name_value_is_usage_error(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                main(["--name"])
        self.assertEqual(raised.exception.code, 2)

    def test_unknown_argument_is_usage_error(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                main(["--unknown"])
        self.assertEqual(raised.exception.code, 2)

    def test_help(self):
        output = io.StringIO()
        with redirect_stdout(output):
            with self.assertRaises(SystemExit) as raised:
                main(["--help"])
        self.assertEqual(raised.exception.code, 0)
        self.assertIn("--name", output.getvalue())
        self.assertIn("--version", output.getvalue())

    def test_version_matches_installed_package(self):
        output = io.StringIO()
        with redirect_stdout(output):
            with self.assertRaises(SystemExit) as raised:
                main(["--version"])
        self.assertEqual(raised.exception.code, 0)
        expected = f"codex-starter {version('gitty473-codex-starter')}\n"
        self.assertEqual(output.getvalue(), expected)

    def test_module_entry_point(self):
        result = subprocess.run(
            [sys.executable, "-m", "codex_starter", "--name", "Andreas"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "Hallo, Andreas!\n")
        self.assertEqual(result.stderr, "")
