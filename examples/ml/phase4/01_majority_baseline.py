"""Majority-class baseline without external dependencies."""
from collections import Counter

def majority_prediction(labels):
    if not labels:
        raise ValueError("labels must not be empty")
    counts = Counter(labels)
    return max(counts, key=lambda label: (counts[label], str(label)))

if __name__ == "__main__":
    y_train = ["yes", "no", "yes", "yes", "no"]
    print("Baseline prediction:", majority_prediction(y_train))