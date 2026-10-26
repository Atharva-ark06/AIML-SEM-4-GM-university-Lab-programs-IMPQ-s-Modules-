"""Cosine similarity for non-zero numeric vectors."""
from math import sqrt

def cosine_similarity(a: list[float], b: list[float]) -> float:
    if len(a) != len(b) or not a:
        raise ValueError("vectors must be non-empty and have equal length")
    norm_a = sqrt(sum(x * x for x in a))
    norm_b = sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        raise ValueError("cosine similarity is undefined for a zero vector")
    return sum(x * y for x, y in zip(a, b)) / (norm_a * norm_b)

if __name__ == "__main__":
    print(cosine_similarity([1, 0], [0.5, 0.5]))
