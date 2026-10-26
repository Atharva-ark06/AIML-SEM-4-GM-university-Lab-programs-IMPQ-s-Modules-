"""Compute binary confusion-matrix counts without external dependencies."""
def confusion_counts(actual, predicted):
    if len(actual) != len(predicted):
        raise ValueError("actual and predicted must have equal length")
    tp = sum(a == 1 and p == 1 for a, p in zip(actual, predicted))
    tn = sum(a == 0 and p == 0 for a, p in zip(actual, predicted))
    fp = sum(a == 0 and p == 1 for a, p in zip(actual, predicted))
    fn = sum(a == 1 and p == 0 for a, p in zip(actual, predicted))
    return {"tn": tn, "fp": fp, "fn": fn, "tp": tp}

if __name__ == "__main__":
    print(confusion_counts([1, 0, 1, 0], [1, 1, 0, 0]))