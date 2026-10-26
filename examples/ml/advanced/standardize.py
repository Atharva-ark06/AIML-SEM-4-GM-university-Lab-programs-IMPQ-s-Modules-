"""Fit and apply a simple standard scaler using training data only."""
from math import sqrt

def fit_standardizer(values: list[float]) -> tuple[float, float]:
    if not values:
        raise ValueError("values cannot be empty")
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    scale = sqrt(variance)
    return mean, scale if scale else 1.0

def transform(values: list[float], mean: float, scale: float) -> list[float]:
    if scale <= 0:
        raise ValueError("scale must be positive")
    return [(x - mean) / scale for x in values]

if __name__ == "__main__":
    train = [10.0, 12.0, 14.0]
    mean, scale = fit_standardizer(train)
    print(transform(train, mean, scale))
