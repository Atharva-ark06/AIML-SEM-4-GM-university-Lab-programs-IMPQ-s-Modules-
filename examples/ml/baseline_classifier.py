"""Compare a simple majority-class baseline with a decision tree."""
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def main():
    data = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.25, random_state=42, stratify=data.target
    )
    for name, model in [
        ("majority baseline", DummyClassifier(strategy="most_frequent")),
        ("decision tree", DecisionTreeClassifier(max_depth=3, random_state=42)),
    ]:
        model.fit(x_train, y_train)
        print(f"{name}: {accuracy_score(y_test, model.predict(x_test)):.3f}")


if __name__ == "__main__":
    main()
