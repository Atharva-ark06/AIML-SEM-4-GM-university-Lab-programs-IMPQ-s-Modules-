"""Illustrate a reproducible train/test split."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def split_dataset(features, target, test_size=0.25, random_state=42):
    """Split examples while preserving class proportions when possible."""
    return train_test_split(
        features, target, test_size=test_size, random_state=random_state, stratify=target
    )


def main():
    data = load_iris()
    x_train, x_test, y_train, y_test = split_dataset(data.data, data.target)
    print("Train rows:", len(x_train), "Test rows:", len(x_test))
    print("Fit learned preprocessing on x_train, never on the combined dataset.")


if __name__ == "__main__":
    main()
