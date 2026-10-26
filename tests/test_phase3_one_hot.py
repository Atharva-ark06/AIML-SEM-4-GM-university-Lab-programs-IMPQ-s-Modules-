from examples.ml.phase3.11_one_hot_encode import one_hot

def test_one_hot_stable_categories():
    labels, matrix = one_hot(["blue", "red", "blue"])
    assert labels == ["blue", "red"]
    assert matrix == [[1, 0], [0, 1], [1, 0]]

def test_one_hot_explicit_category_order():
    labels, matrix = one_hot(["red"], ["red", "blue"])
    assert matrix == [[1, 0]]
