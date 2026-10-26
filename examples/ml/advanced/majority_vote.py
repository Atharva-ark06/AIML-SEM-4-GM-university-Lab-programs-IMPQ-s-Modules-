"""Combine class predictions with deterministic majority voting."""
from collections import Counter

def majority_vote(predictions: list[object]) -> object:
    if not predictions:
        raise ValueError("predictions cannot be empty")
    counts = Counter(predictions)
    highest = max(counts.values())
    tied = [label for label, count in counts.items() if count == highest]
    return sorted(tied, key=repr)[0]

if __name__ == "__main__":
    print(majority_vote(["A", "B", "A", "B", "A"]))
