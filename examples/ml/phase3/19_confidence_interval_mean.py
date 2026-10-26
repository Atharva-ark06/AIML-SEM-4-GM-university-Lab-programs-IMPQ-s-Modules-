"""Illustrative normal-approximation interval for a sample mean."""
from math import sqrt

def mean_interval(values, z=1.96):
    if len(values) < 2:
        raise ValueError("at least two values are required")
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    margin = z * sqrt(variance / len(values))
    return mean - margin, mean + margin

if __name__ == "__main__":
    print(mean_interval([4, 5, 6, 5, 7]))