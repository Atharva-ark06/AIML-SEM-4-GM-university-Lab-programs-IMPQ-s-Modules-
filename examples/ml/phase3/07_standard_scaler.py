"""Fit a simple standardizer and reuse its training statistics."""
from math import sqrt

def fit_standardizer(values):
    if not values:
        raise ValueError("values must not be empty")
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return mean, sqrt(variance)

def transform(values, mean, std):
    if std == 0:
        return [0.0 for _ in values]
    return [(x - mean) / std for x in values]

if __name__ == "__main__":
    stats = fit_standardizer([2, 4, 6])
    print(stats, transform([2, 4, 6], *stats))