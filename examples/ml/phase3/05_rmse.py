"""Root mean squared error for numeric predictions."""
from math import sqrt

def root_mean_squared_error(actual, predicted):
    if not actual or len(actual) != len(predicted):
        raise ValueError("provide equal, non-empty sequences")
    return sqrt(sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual))

if __name__ == "__main__":
    print(root_mean_squared_error([3, 5, 2], [2, 5, 4]))