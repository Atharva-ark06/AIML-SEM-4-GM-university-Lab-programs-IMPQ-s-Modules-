"""Cosine similarity with a zero-vector guard."""
from math import sqrt

def cosine_similarity(left, right):
    if len(left) != len(right):
        raise ValueError("vectors must have equal dimensions")
    norm_l = sqrt(sum(x * x for x in left))
    norm_r = sqrt(sum(x * x for x in right))
    if not norm_l or not norm_r:
        return 0.0
    return sum(a * b for a, b in zip(left, right)) / (norm_l * norm_r)

if __name__ == "__main__":
    print(cosine_similarity([1, 0], [0.8, 0.2]))