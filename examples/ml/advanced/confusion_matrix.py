"""Build a confusion matrix for integer class labels."""
from collections import Counter

def confusion_matrix(y_true: list[int], y_pred: list[int], labels: list[int] | None = None) -> list[list[int]]:
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("label lists must be non-empty and equal length")
    if labels is None:
        labels = sorted(set(y_true) | set(y_pred))
    index = {label: i for i, label in enumerate(labels)}
    if any(label not in index for label in y_true + y_pred):
        raise ValueError("labels list omits a seen class")
    matrix = [[0 for _ in labels] for _ in labels]
    for actual, predicted in zip(y_true, y_pred):
        matrix[index[actual]][index[predicted]] += 1
    return matrix

if __name__ == "__main__":
    print(confusion_matrix([0, 1, 1, 0], [0, 1, 0, 0]))
