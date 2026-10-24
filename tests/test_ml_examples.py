import numpy as np
from examples.ml.minmax_scaling import scale_features
from examples.ml.standardization import standardize
from examples.ml.missing_values import impute_training_features
from examples.ml.feature_encoding import encode_categories


def test_minmax_scaling_maps_training_range_to_zero_one():
    scaled = scale_features([[1, 10], [2, 20], [3, 30]])
    assert np.allclose(scaled.min(axis=0), [0, 0])
    assert np.allclose(scaled.max(axis=0), [1, 1])


def test_standardization_has_zero_column_means():
    scaled = standardize([[1, 10], [2, 20], [3, 30]])
    assert np.allclose(scaled.mean(axis=0), [0, 0])


def test_imputation_uses_training_data_and_fills_missing_values():
    train, test = impute_training_features([[1, 10], [np.nan, 20], [3, 30]], [[np.nan, 25]])
    assert not np.isnan(train).any()
    assert not np.isnan(test).any()
    assert test.shape == (1, 2)


def test_one_hot_encoding_produces_expected_shape():
    encoded, names = encode_categories(["budget", "premium", "budget"])
    assert encoded.shape == (3, 2)
    assert len(names) == 2
