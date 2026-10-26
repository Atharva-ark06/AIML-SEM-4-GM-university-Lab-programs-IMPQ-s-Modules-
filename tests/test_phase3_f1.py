from examples.ml.phase3.03_f1_score import f1_score

def test_f1_score():
    assert round(f1_score(0.8, 0.6), 6) == round(0.6857142857, 6)

def test_f1_zero():
    assert f1_score(0, 0) == 0.0
