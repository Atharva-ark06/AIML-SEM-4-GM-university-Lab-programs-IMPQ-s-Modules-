"""Separate target and feature columns from row dictionaries."""
from collections.abc import Mapping, Sequence

def split_target(rows: Sequence[Mapping[str, object]], target: str) -> tuple[list[dict[str, object]], list[object]]:
    if not rows:
        raise ValueError("rows cannot be empty")
    if any(target not in row for row in rows):
        raise KeyError(f"target column {target!r} missing from at least one row")
    features = [{key: value for key, value in row.items() if key != target} for row in rows]
    labels = [row[target] for row in rows]
    return features, labels

if __name__ == "__main__":
    X, y = split_target([{"hours": 2, "passed": 0}, {"hours": 5, "passed": 1}], "passed")
    print(X, y)
