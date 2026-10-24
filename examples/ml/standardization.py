"""Demonstrate standardization (z-score scaling)."""
import numpy as np
from sklearn.preprocessing import StandardScaler


def standardize(values):
    """Return standardized values; each column is scaled independently."""
    array = np.asarray(values, dtype=float)
    if array.ndim != 2:
        raise ValueError("Expected a two-dimensional feature matrix")
    return StandardScaler().fit_transform(array)


def main():
    print(standardize([[10, 1], [20, 2], [30, 3]]).round(3))


if __name__ == "__main__":
    main()
