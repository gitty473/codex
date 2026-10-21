"""Tests der unabhängig nutzbaren Anwendungslogik."""

import unittest

from codex_starter.greeting import build_greeting


class GreetingTests(unittest.TestCase):
    def test_default_name(self):
        self.assertEqual(build_greeting(), "Hallo, Welt!")

    def test_custom_name(self):
        self.assertEqual(build_greeting("Andreas"), "Hallo, Andreas!")

    def test_trims_surrounding_whitespace(self):
        self.assertEqual(build_greeting("  Andreas\t"), "Hallo, Andreas!")

    def test_preserves_unicode(self):
        self.assertEqual(build_greeting("Jörg"), "Hallo, Jörg!")

    def test_rejects_empty_names(self):
        for name in ("", " ", "\t\n"):
            with self.subTest(name=name):
                with self.assertRaisesRegex(ValueError, "nicht leer"):
                    build_greeting(name)
