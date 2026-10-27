"""Precision with an explicit zero-denominator policy."""
def precision(tp, fp):
    denominator = tp + fp
    return tp / denominator if denominator else 0.0

if __name__ == "__main__":
    print(precision(7, 3))