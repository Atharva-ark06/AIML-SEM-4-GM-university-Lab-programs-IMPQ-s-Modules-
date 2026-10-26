"""Accuracy score with input validation."""
def accuracy(y_true: list[object], y_pred: list[object]) -> float:
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("label lists must be non-empty and equal length")
    return sum(a == b for a, b in zip(y_true, y_pred)) / len(y_true)

if __name__ == "__main__":
    print(accuracy(["cat", "dog", "cat"], ["cat", "cat", "cat"]))
