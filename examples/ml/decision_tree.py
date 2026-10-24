"""Decision tree classification with a held-out test set."""
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def main():
    data = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.25, random_state=21, stratify=data.target
    )
    model = DecisionTreeClassifier(max_depth=3, random_state=21)
    model.fit(x_train, y_train)
    print("Test accuracy:", round(accuracy_score(y_test, model.predict(x_test)), 3))
    print("Depth limit:", model.get_depth())


if __name__ == "__main__":
    main()
