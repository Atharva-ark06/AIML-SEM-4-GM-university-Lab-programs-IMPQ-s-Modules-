"""Demonstrate stratified cross-validation on Iris."""
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


def main():
    data = load_iris()
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    scores = cross_val_score(model, data.data, data.target, cv=folds, scoring="accuracy")
    print("Fold scores:", scores.round(3).tolist())
    print("Mean accuracy:", round(float(scores.mean()), 3))


if __name__ == "__main__":
    main()
