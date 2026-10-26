"""Deterministic split helper for small teaching datasets."""
import random
from typing import TypeVar
T = TypeVar("T")

def split(items: list[T], test_fraction: float = 0.2, seed: int = 42) -> tuple[list[T], list[T]]:
    if not 0 < test_fraction < 1:
        raise ValueError("test_fraction must be strictly between 0 and 1")
    if len(items) < 2:
        raise ValueError("at least two items are required")
    indexes = list(range(len(items)))
    random.Random(seed).shuffle(indexes)
    n_test = min(len(items) - 1, max(1, round(len(items) * test_fraction)))
    test_idx = set(indexes[:n_test])
    return [x for i, x in enumerate(items) if i not in test_idx], [x for i, x in enumerate(items) if i in test_idx]

if __name__ == "__main__":
    print(split(list(range(10))))
