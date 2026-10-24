"""Show a simple variance-based feature inspection."""
import numpy as np
from sklearn.feature_selection import VarianceThreshold


def remove_constant_features(values, threshold=0.0):
    """Return transformed matrix and the fitted selector."""
    selector = VarianceThreshold(threshold=threshold)
    return selector.fit_transform(np.asarray(values, dtype=float)), selector


def main():
    x = [[1, 5, 0], [2, 5, 1], [3, 5, 0]]
    transformed, selector = remove_constant_features(x)
    print("Before:", len(x[0]), "features")
    print("After:", transformed.shape[1])
    print("Kept mask:", selector.get_support().tolist())


if __name__ == "__main__":
    main()
