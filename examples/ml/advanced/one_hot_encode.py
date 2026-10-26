"""Simple deterministic one-hot encoding for categorical values."""
from collections.abc import Sequence

def one_hot(values: Sequence[str], categories: Sequence[str] | None = None) -> tuple[list[str], list[list[int]]]:
    if categories is None:
        categories = sorted(set(values))
    if len(set(categories)) != len(categories):
        raise ValueError("categories must be unique")
    unknown = set(values) - set(categories)
    if unknown:
        raise ValueError(f"unknown categories: {sorted(unknown)}")
    matrix = [[int(value == category) for category in categories] for value in values]
    return list(categories), matrix

if __name__ == "__main__":
    columns, matrix = one_hot(["red", "blue", "red"])
    print(columns)
    print(matrix)
