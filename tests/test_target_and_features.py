import pandas as pd
import pytest
from examples.ml.target_and_features import split_target


def test_target_is_removed_from_features():
    frame = pd.DataFrame({"distance": [1, 2], "cost": [10, 20]})
    x, y = split_target(frame, "cost")
    assert list(x.columns) == ["distance"]
    assert y.tolist() == [10, 20]


def test_missing_target_column_is_rejected():
    with pytest.raises(KeyError):
        split_target(pd.DataFrame({"x": [1]}), "label")
