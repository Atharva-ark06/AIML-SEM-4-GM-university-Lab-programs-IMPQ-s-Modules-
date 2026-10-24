"""Compile maintained Python examples and tests without executing them."""
from pathlib import Path
import py_compile
import sys


ROOT = Path(__file__).resolve().parents[1]
TARGETS = [ROOT / "examples", ROOT / "tests", ROOT / "scripts"]


def main():
    files = sorted(path for target in TARGETS for path in target.rglob("*.py"))
    failures = []
    for path in files:
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as error:
            failures.append((path, str(error)))
    for path, error in failures:
        print(f"FAIL {path.relative_to(ROOT)}: {error}")
    print(f"Checked {len(files)} Python files; failures: {len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
