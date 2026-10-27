"""Binary confusion-matrix counts with positive label 1."""
def confusion_counts(y_true, y_pred, positive=1):
    if len(y_true) != len(y_pred):
        raise ValueError("lengths must match")
    tp = fp = tn = fn = 0
    for actual, predicted in zip(y_true, y_pred):
        if actual == positive and predicted == positive: tp += 1
        elif actual != positive and predicted == positive: fp += 1
        elif actual != positive and predicted != positive: tn += 1
        else: fn += 1
    return {"tp": tp, "fp": fp, "tn": tn, "fn": fn}

if __name__ == "__main__":
    print(confusion_counts([1, 0, 1, 0], [1, 1, 0, 0]))