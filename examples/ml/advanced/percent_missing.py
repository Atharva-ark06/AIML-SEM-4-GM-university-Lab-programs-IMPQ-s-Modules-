"""Report missing counts and percentages for column sequences."""
from collections.abc import Mapping, Sequence
from math import isnan

def missing_report(columns: Mapping[str, Sequence[object]]) -> dict[str, dict[str, float | int]]:
    report: dict[str, dict[str, float | int]] = {}
    for name, values in columns.items():
        missing = sum(v is None or (isinstance(v, float) and isnan(v)) for v in values)
        total = len(values)
        report[name] = {"missing_count": missing, "missing_percent": 100 * missing / total if total else 0.0}
    return report

if __name__ == "__main__":
    print(missing_report({"age": [20, None, 22], "score": [None, None, 9]}))
