"""Precision and recall with safe zero-denominator handling."""
def precision_recall(tp, fp, fn):
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return precision, recall

if __name__ == "__main__":
    print(precision_recall(tp=8, fp=2, fn=3))