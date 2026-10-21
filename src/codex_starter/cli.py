"""Kommandozeileneinstiegspunkt für das Scaffold."""

import argparse
from collections.abc import Sequence
from importlib.metadata import version

from .greeting import build_greeting


def main(argv: Sequence[str] | None = None) -> int:
    """Verarbeite Argumente und gib eine Begrüßung aus."""
    parser = argparse.ArgumentParser(
        prog="codex-starter",
        description="Eine kleine, erweiterbare Python-Beispielanwendung.",
    )
    parser.add_argument("--name", default="Welt", help="Name für die Begrüßung")
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version('gitty473-codex-starter')}",
    )
    args = parser.parse_args(argv)

    try:
        greeting = build_greeting(args.name)
    except ValueError as exc:
        parser.error(str(exc))

    print(greeting)
    return 0
