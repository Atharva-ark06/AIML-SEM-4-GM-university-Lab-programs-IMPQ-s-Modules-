"""Compare robust scaling with unscaled features."""
from sklearn.preprocessing import RobustScaler


def robust_scale(values):
    """Scale each feature using its median and interquartile range."""
    return RobustScaler().fit_transform(values)


def main():
    values = [[1.0], [2.0], [3.0], [100.0]]
    print("Robust-scaled values:", robust_scale(values).ravel().round(3).tolist())


if __name__ == "__main__":
    main()
