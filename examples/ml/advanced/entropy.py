"""Calculate Shannon entropy for a non-empty sequence of labels."""
from collections import Counter
from math import log2
from typing import Hashable, Iterable

def entropy(labels: Iterable[Hashable]) -> float:
    counts = Counter(labels)
    total = sum(counts.values())
    if total == 0:
        raise ValueError("labels cannot be empty")
    return -sum((count / total) * log2(count / total) for count in counts.values())

if __name__ == "__main__":
    print("balanced binary:", entropy([0, 0, 1, 1]))
    print("pure:", entropy(["yes", "yes", "yes"]))
