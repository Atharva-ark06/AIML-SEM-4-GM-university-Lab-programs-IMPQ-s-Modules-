from examples.ml.phase3.18_brier_score import brier_score
import pytest

def test_brier_score():
    assert round(brier_score([0, 1, 1], [0.1, 0.7, 0.8]), 6) == 0.02

def test_brier_rejects_invalid_probability():
    with pytest.raises(ValueError):
        brier_score([1], [1.5])
