"""Print a compact inventory of course resources without modifying files."""
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    paths = sorted(path for path in ROOT.rglob("*") if path.is_file()
                   and not any(part in {".git", ".venv", "__pycache__"} for part in path.parts))
    categories = {
        "Python": {".py"},
        "PDF": {".pdf"},
        "Slides": {".ppt", ".pptx"},
        "Documents": {".doc", ".docx"},
        "Data": {".csv", ".tsv", ".json"},
        "Markdown": {".md"},
    }
    for label, suffixes in categories.items():
        matches = [path for path in paths if path.suffix.lower() in suffixes]
        print(f"{label:10} {len(matches):3}")
        for path in matches[:12]:
            print("  -", path.relative_to(ROOT))
        if len(matches) > 12:
            print(f"  ... and {len(matches) - 12} more")


if __name__ == "__main__":
    main()
