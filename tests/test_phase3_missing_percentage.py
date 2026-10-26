from importlib import import_module
missing_percentage = import_module("examples.ml.phase3.09_missing_percentage").missing_percentage

def test_missing_percentage():
    assert missing_percentage([1, None, None, 4]) == 50.0

def test_empty_missing_percentage():
    assert missing_percentage([]) == 0.0
