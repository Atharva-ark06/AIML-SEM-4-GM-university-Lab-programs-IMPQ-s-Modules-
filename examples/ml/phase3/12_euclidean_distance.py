"""Euclidean distance between two equal-dimensional vectors."""
from math import sqrt

def euclidean_distance(left, right):
    if len(left) != len(right):
        raise ValueError("vectors must have equal dimensions")
    return sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))

if __name__ == "__main__":
    print(euclidean_distance([1, 2], [4, 6]))