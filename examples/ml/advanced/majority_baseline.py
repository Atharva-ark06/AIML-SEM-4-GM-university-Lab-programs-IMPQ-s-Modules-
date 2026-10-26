"""Majority-class baseline predictor for labels."""
from collections import Counter
from typing import TypeVar
T = TypeVar("T")

def fit_majority(labels: list[T]) -> T:
    if not labels:
        raise ValueError("labels cannot be empty")
    counts = Counter(labels)
    return max(counts, key=lambda label: (counts[label], repr(label)))

def predict_majority(labels: list[T], n: int) -> list[T]:
    if n < 0:
        raise ValueError("n cannot be negative")
    return [fit_majority(labels) for _ in range(n)]

if __name__ == "__main__":
    print(predict_majority(["pass", "fail", "pass"], 4))
