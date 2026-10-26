"""Pearson correlation coefficient for paired numeric samples."""
from math import sqrt

def pearson(x: list[float], y: list[float]) -> float:
    if len(x) != len(y) or len(x) < 2:
        raise ValueError("paired lists must have equal length of at least two")
    mx, my = sum(x) / len(x), sum(y) / len(y)
    dx, dy = [v - mx for v in x], [v - my for v in y]
    denominator = sqrt(sum(v * v for v in dx) * sum(v * v for v in dy))
    if denominator == 0:
        raise ValueError("correlation is undefined for a constant input")
    return sum(a * b for a, b in zip(dx, dy)) / denominator

if __name__ == "__main__":
    print(pearson([1, 2, 3], [2, 4, 6]))
