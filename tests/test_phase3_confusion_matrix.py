from examples.ml.phase3.01_confusion_matrix import confusion_counts

def test_confusion_counts():
    assert confusion_counts([1, 0, 1, 0], [1, 1, 0, 0]) == {"tn": 1, "fp": 1, "fn": 1, "tp": 1}
