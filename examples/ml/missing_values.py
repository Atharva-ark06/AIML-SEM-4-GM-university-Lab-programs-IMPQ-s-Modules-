"""Demonstrate median imputation without using test-set statistics."""
import numpy as np
from sklearn.impute import SimpleImputer


def impute_training_features(train_values, test_values):
    """Fit median imputation on train data and apply it to test data."""
    imputer = SimpleImputer(strategy="median")
    train_array = np.asarray(train_values, dtype=float)
    test_array = np.asarray(test_values, dtype=float)
    return imputer.fit_transform(train_array), imputer.transform(test_array)


def main():
    train = [[1.0, 10.0], [np.nan, 20.0], [3.0, 30.0]]
    test = [[np.nan, 25.0]]
    x_train, x_test = impute_training_features(train, test)
    print("Imputed train:\n", x_train)
    print("Imputed test:\n", x_test)


if __name__ == "__main__":
    main()
