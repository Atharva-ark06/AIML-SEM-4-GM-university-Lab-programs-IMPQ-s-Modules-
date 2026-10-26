"""Shannon entropy in bits for a sequence of class labels."""
from math import log2

def entropy(labels):
    if not labels:
        return 0.0
    return -sum((count / len(labels)) * log2(count / len(labels))
                for count in {label: labels.count(label) for label in set(labels)}.values())

if __name__ == "__main__":
    print(entropy(["yes", "yes", "no", "no"]))