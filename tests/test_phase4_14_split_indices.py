from importlib import import_module
import pytest
m=import_module("examples.ml.phase4.24_split_indices")
def test_split_indices():
    train,test=m.split_indices(10,0.2)
    assert train==list(range(8)) and test==[8,9]
def test_split_requires_two_items():
    with pytest.raises(ValueError): m.split_indices(1)