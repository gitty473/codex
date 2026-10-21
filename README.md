# codex

Erweiterbare Python-Projektbasis mit einem kleinen, ausführbaren CLI-Beispiel.
Ein fachlicher Anwendungszweck ist noch nicht festgelegt. Das Scaffold trennt
Anwendungslogik, Kommandozeile und Tests und benötigt keine Laufzeitabhängigkeiten
außer der Python-Standardbibliothek.

## Voraussetzungen

- Python 3.11 oder neuer mit `pip` und `venv`
- Git zum Klonen des Repositorys

## Schnellstart

```sh
git clone https://github.com/gitty473/codex.git
cd codex
python -m venv .venv
```

Virtuelle Umgebung aktivieren:

```sh
# Linux / macOS
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Je nach System heißt der Python-Befehl vor der Aktivierung `python3` oder `py`.
Anschließend das Paket im Entwicklungsmodus installieren:

```sh
python -m pip install -e .
codex-starter
# Hallo, Welt!
codex-starter --name Andreas
# Hallo, Andreas!
python -m codex_starter --name Andreas
# Hallo, Andreas!
```

`--help` zeigt die verfügbaren Optionen, `--version` die Paketversion. Namen
werden an den Rändern von Leerraum bereinigt; leere Namen werden mit Exitcode 2
und einer Fehlermeldung abgewiesen. Erfolgreiche Aufrufe liefern Exitcode 0.

## Projektstruktur

```text
.editorconfig               Einheitliche Editor-Grundeinstellungen
.github/workflows/ci.yml     Automatische Tests und Paketprüfung
.gitignore                  Ausschluss lokaler und erzeugter Dateien
.gitkeep                    Vorhandener Platzhalter, unverändert erhalten
LICENSE                     MIT-Lizenz
README.md                   Einrichtung, Nutzung und Entwicklung
pyproject.toml              Paketmetadaten, Build und CLI-Einstiegspunkt
src/codex_starter/
    __init__.py             Paketbeschreibung
    __main__.py             Aufruf über python -m codex_starter
    cli.py                  Argumentverarbeitung und Ausgabe
    greeting.py             Unabhängige Beispiel-Anwendungslogik
tests/
    test_cli.py             CLI- und Prozessintegrationstests
    test_greeting.py        Tests der Anwendungslogik
```

## Entwicklung und Prüfung

Nach der Installation im Entwicklungsmodus:

```sh
python -m unittest discover -s tests -v
```

Ein installierbares Wheel erzeugen:

```sh
python -m pip wheel --no-deps --wheel-dir dist .
```

Der Build verwendet `setuptools`; `pip` installiert die benötigte Build-Version
bei Bedarf in einer isolierten Umgebung. Für die Tests sind keine zusätzlichen
Pakete erforderlich.

GitHub Actions führt bei Pushes auf `main`, Pull Requests nach `main` und
manuellem Start Tests unter Python 3.11 und 3.14 aus. Zusätzlich wird ein Wheel
gebaut und in einer frischen virtuellen Umgebung auf beide CLI-Einstiegspunkte
geprüft. Die verwendeten Actions sind auf konkrete Commit-SHAs fixiert.

Neue Anwendungslogik gehört nach `src/codex_starter/`, zugehörige Tests nach
`tests/`. Die CLI bleibt in `cli.py`. Paketname und Version sind zentral in
`pyproject.toml` definiert; die CLI liest die installierte Paketversion daraus.
Vor einem Commit Tests ausführen und die Dokumentation bei Verhaltensänderungen
aktualisieren.

## Lizenz

MIT, siehe [LICENSE](LICENSE). Copyright (c) 2026 gitty473.
