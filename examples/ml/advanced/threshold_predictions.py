"""Convert probabilities into binary predictions at a threshold."""
def threshold_predictions(probabilities: list[float], threshold: float = 0.5) -> list[int]:
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between zero and one")
    if any(not 0 <= p <= 1 for p in probabilities):
        raise ValueError("probabilities must be between zero and one")
    return [int(p >= threshold) for p in probabilities]

if __name__ == "__main__":
    print(threshold_predictions([0.1, 0.49, 0.5, 0.9]))
