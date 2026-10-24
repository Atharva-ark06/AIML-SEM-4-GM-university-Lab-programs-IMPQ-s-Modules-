"""KNN classification using a small, reproducible synthetic dataset."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


def main():
    data = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.25, random_state=42, stratify=data.target
    )
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print("Accuracy:", round(accuracy_score(y_test, predictions), 3))
    print("Pipeline keeps scaling fitted on training data only.")


if __name__ == "__main__":
    main()
