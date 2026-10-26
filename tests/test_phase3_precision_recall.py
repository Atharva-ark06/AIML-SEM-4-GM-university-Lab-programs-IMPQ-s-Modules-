from examples.ml.phase3.02_precision_recall import precision_recall

def test_precision_recall():
    assert precision_recall(8, 2, 3) == (0.8, 8 / 11)

def test_zero_denominator():
    assert precision_recall(0, 0, 0) == (0.0, 0.0)
