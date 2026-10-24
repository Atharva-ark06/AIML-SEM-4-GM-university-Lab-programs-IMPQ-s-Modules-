"""Demonstrate a reproducible validation-score comparison."""
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier


def main():
    data = load_iris()
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=9)
    for depth in (1, 2, 3, None):
        model = DecisionTreeClassifier(max_depth=depth, random_state=9)
        scores = cross_val_score(model, data.data, data.target, cv=cv, scoring="accuracy")
        print(f"max_depth={depth!s:>4}: mean={scores.mean():.3f}, std={scores.std():.3f}")


if __name__ == "__main__":
    main()
