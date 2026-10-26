from examples.ml.phase3.06_train_test_indices import split_indices
import pytest

def test_split_indices_cover_rows():
    train, test = split_indices(10, 0.3)
    assert train == list(range(7))
    assert test == [7, 8, 9]

def test_split_rejects_invalid_fraction():
    with pytest.raises(ValueError):
        split_indices(10, 1.0)
