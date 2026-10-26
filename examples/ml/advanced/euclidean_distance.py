"""Euclidean distance between equally sized numeric vectors."""
from math import sqrt

def euclidean(a: list[float], b: list[float]) -> float:
    if len(a) != len(b) or not a:
        raise ValueError("vectors must be non-empty and have equal length")
    return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

if __name__ == "__main__":
    print(euclidean([1, 2], [4, 6]))
