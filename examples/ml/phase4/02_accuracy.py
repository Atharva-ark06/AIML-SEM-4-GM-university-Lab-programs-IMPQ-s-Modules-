"""Compute classification accuracy."""
def accuracy(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("lengths must match")
    if not y_true:
        raise ValueError("inputs must not be empty")
    return sum(a == b for a, b in zip(y_true, y_pred)) / len(y_true)

if __name__ == "__main__":
    print(accuracy([1, 0, 1, 1], [1, 1, 1, 0]))