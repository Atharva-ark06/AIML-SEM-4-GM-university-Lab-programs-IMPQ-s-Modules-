"""Gaussian Naive Bayes classification on the Iris dataset."""
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def main():
    data = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.25, random_state=17, stratify=data.target
    )
    model = GaussianNB().fit(x_train, y_train)
    print(classification_report(y_test, model.predict(x_test), target_names=data.target_names))


if __name__ == "__main__":
    main()
