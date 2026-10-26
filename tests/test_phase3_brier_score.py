from importlib import import_module
brier_score = import_module("examples.ml.phase3.18_brier_score").brier_score
import pytest

def test_brier_score():
    assert round(brier_score([0, 1, 1], [0.1, 0.7, 0.8]), 6) == round(0.14 / 3, 6)

def test_brier_rejects_invalid_probability():
    with pytest.raises(ValueError):
        brier_score([1], [1.5])
