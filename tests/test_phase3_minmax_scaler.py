from importlib import import_module
fit_minmax = import_module("examples.ml.phase3.08_minmax_scaler").fit_minmax
transform = import_module("examples.ml.phase3.08_minmax_scaler").transform

def test_minmax_training_bounds():
    low, high = fit_minmax([10, 20, 30])
    assert transform([10, 20, 30], low, high) == [0.0, 0.5, 1.0]

def test_constant_minmax_values():
    low, high = fit_minmax([5, 5])
    assert transform([5, 6], low, high) == [0.0, 0.0]
