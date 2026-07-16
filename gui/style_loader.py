from pathlib import Path


def load_stylesheet():

    styles_dir = Path("assets/styles")

    parts = []

    for file in sorted(styles_dir.glob("*.qss")):
        parts.append(file.read_text(encoding="utf-8"))

    return "\n".join(parts)