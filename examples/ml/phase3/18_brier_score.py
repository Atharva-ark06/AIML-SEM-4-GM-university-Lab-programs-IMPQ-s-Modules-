"""Brier score for binary outcomes and predicted probabilities."""
def brier_score(actual, probabilities):
    if not actual or len(actual) != len(probabilities):
        raise ValueError("provide equal, non-empty sequences")
    if any(y not in (0, 1) for y in actual):
        raise ValueError("actual labels must be binary 0/1")
    if any(not 0 <= p <= 1 for p in probabilities):
        raise ValueError("probabilities must be in [0, 1]")
    return sum((y - p) ** 2 for y, p in zip(actual, probabilities)) / len(actual)

if __name__ == "__main__":
    print(brier_score([0, 1, 1], [0.1, 0.7, 0.8]))