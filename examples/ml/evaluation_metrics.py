"""Compute common classification metrics on a held-out dataset."""
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def main():
    data = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.25, random_state=12, stratify=data.target
    )
    model = DecisionTreeClassifier(max_depth=3, random_state=12).fit(x_train, y_train)
    predicted = model.predict(x_test)
    print("Accuracy:", round(accuracy_score(y_test, predicted), 3))
    print("Macro precision:", round(precision_score(y_test, predicted, average="macro", zero_division=0), 3))
    print("Macro recall:", round(recall_score(y_test, predicted, average="macro", zero_division=0), 3))
    print("Macro F1:", round(f1_score(y_test, predicted, average="macro", zero_division=0), 3))


if __name__ == "__main__":
    main()
