from importlib import import_module
root_mean_squared_error = import_module("examples.ml.phase3.05_rmse").root_mean_squared_error
import pytest

def test_rmse():
    assert round(root_mean_squared_error([3, 5, 2], [2, 5, 4]), 6) == round((5 / 3) ** 0.5, 6)

def test_rmse_rejects_mismatch():
    with pytest.raises(ValueError):
        root_mean_squared_error([1], [1, 2])
