"""Recall with an explicit zero-denominator policy."""
def recall(tp, fn):
    denominator = tp + fn
    return tp / denominator if denominator else 0.0

if __name__ == "__main__":
    print(recall(7, 2))