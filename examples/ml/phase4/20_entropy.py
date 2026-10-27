"""Shannon entropy in bits for discrete observations."""
from collections import Counter
from math import log2
def entropy(values):
    if not values: raise ValueError("values must not be empty")
    counts=Counter(values); n=len(values)
    return -sum((c/n)*log2(c/n) for c in counts.values())
if __name__ == "__main__": print(entropy(["A","A","B","B"]))