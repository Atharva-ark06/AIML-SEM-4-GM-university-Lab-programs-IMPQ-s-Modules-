"""Mean absolute error for equal-length numeric sequences."""
def mean_absolute_error(actual, predicted):
    if not actual or len(actual) != len(predicted):
        raise ValueError("provide equal, non-empty sequences")
    return sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual)

if __name__ == "__main__":
    print(mean_absolute_error([3, 5, 2], [2, 5, 4]))