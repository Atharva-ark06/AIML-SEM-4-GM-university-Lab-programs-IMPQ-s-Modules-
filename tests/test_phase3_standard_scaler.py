from importlib import import_module
fit_standardizer = import_module("examples.ml.phase3.07_standard_scaler").fit_standardizer
transform = import_module("examples.ml.phase3.07_standard_scaler").transform

def test_standardizer_centers_values():
    mean, std = fit_standardizer([2, 4, 6])
    assert mean == 4
    assert transform([4], mean, std) == [0.0]

def test_constant_values_transform_to_zero():
    mean, std = fit_standardizer([3, 3, 3])
    assert transform([3, 4], mean, std) == [0.0, 0.0]
