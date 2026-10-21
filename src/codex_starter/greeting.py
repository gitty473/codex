"""Anwendungslogik ohne Abhängigkeit von der Kommandozeile."""


def build_greeting(name: str = "Welt") -> str:
    """Erzeuge eine Begrüßung; lehne Namen ohne sichtbare Zeichen ab."""
    normalized_name = name.strip()
    if not normalized_name:
        raise ValueError("Der Name darf nicht leer sein.")
    return f"Hallo, {normalized_name}!"
