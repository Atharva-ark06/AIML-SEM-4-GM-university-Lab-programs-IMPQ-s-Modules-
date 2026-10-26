"""Precision, recall, and F1 for binary labels encoded as 0/1."""

def score(y_true: list[int], y_pred: list[int]) -> dict[str, float]:
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("label lists must be non-empty and equal length")
    if any(v not in (0, 1) for v in y_true + y_pred):
        raise ValueError("labels must be encoded as 0 or 1")
    tp = sum(a == 1 and b == 1 for a, b in zip(y_true, y_pred))
    fp = sum(a == 0 and b == 1 for a, b in zip(y_true, y_pred))
    fn = sum(a == 1 and b == 0 for a, b in zip(y_true, y_pred))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}

if __name__ == "__main__":
    print(score([1, 0, 1, 1, 0], [1, 0, 0, 1, 1]))
