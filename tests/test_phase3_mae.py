from examples.ml.phase3.04_mae import mean_absolute_error
import pytest

def test_mae():
    assert mean_absolute_error([3, 5, 2], [2, 5, 4]) == 1.0

def test_mae_rejects_empty():
    with pytest.raises(ValueError):
        mean_absolute_error([], [])
