"""Compute basic classification metrics from a 2x2 confusion matrix."""

def metrics_from_counts(tp: int, fp: int, fn: int, tn: int) -> dict[str, float]:
    values = (tp, fp, fn, tn)
    if any(not isinstance(v, int) or v < 0 for v in values):
        raise ValueError("confusion counts must be non-negative integers")
    total = tp + fp + fn + tn
    if total == 0:
        raise ValueError("at least one observation is required")
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"accuracy": (tp + tn) / total, "precision": precision, "recall": recall, "f1": f1}

if __name__ == "__main__":
    print(metrics_from_counts(tp=42, fp=8, fn=10, tn=40))
