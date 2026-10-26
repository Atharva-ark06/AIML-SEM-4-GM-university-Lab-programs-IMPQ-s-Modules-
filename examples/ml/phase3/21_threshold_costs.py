"""Compare candidate probability thresholds by simple weighted error cost."""
def threshold_cost(actual, probabilities, threshold, false_positive_cost=1.0, false_negative_cost=1.0):
    if len(actual) != len(probabilities) or not actual:
        raise ValueError("actual and probabilities must be equal, non-empty sequences")
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be in [0, 1]")
    if false_positive_cost < 0 or false_negative_cost < 0:
        raise ValueError("error costs must be non-negative")
    fp = sum(y == 0 and p >= threshold for y, p in zip(actual, probabilities))
    fn = sum(y == 1 and p < threshold for y, p in zip(actual, probabilities))
    return fp * false_positive_cost + fn * false_negative_cost

if __name__ == "__main__":
    actual = [0, 1, 1, 0]
    probabilities = [0.2, 0.45, 0.8, 0.7]
    for threshold in (0.3, 0.5, 0.7):
        print(threshold, threshold_cost(actual, probabilities, threshold, 1, 3))
