"""Mean absolute error and root mean squared error."""
from math import sqrt

def regression_errors(actual: list[float], predicted: list[float]) -> dict[str, float]:
    if len(actual) != len(predicted) or not actual:
        raise ValueError("actual and predicted must be non-empty and equal length")
    errors = [a - p for a, p in zip(actual, predicted)]
    mae = sum(abs(e) for e in errors) / len(errors)
    rmse = sqrt(sum(e * e for e in errors) / len(errors))
    return {"mae": mae, "rmse": rmse}

if __name__ == "__main__":
    print(regression_errors([3, -0.5, 2, 7], [2.5, 0, 2, 8]))
