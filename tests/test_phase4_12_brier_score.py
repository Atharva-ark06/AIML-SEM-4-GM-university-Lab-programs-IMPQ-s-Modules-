from importlib import import_module
import pytest
m=import_module("examples.ml.phase4.22_brier_score")
def test_brier_score(): assert m.brier_score([0,1,1],[0.1,0.8,0.6])==pytest.approx(0.07)
def test_probability_range():
    with pytest.raises(ValueError): m.brier_score([1],[1.2])