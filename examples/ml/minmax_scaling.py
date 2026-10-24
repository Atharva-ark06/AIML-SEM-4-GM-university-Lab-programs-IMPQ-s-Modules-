"""Demonstrate min-max scaling with scikit-learn."""
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def scale_features(values):
    """Fit and apply MinMaxScaler to a 2D array."""
    array = np.asarray(values, dtype=float)
    if array.ndim != 2:
        raise ValueError("Expected a two-dimensional feature matrix")
    return MinMaxScaler().fit_transform(array)


def main():
    values = [[10, 100], [20, 150], [30, 200]]
    print(scale_features(values))


if __name__ == "__main__":
    main()
