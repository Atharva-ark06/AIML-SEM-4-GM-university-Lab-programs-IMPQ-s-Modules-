"""KNN regression on a tiny synthetic one-feature dataset."""
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor


def main():
    x_train = np.array([[10], [20], [30], [40], [50]], dtype=float)
    y_train = np.array([100, 190, 310, 390, 510], dtype=float)
    model = KNeighborsRegressor(n_neighbors=2).fit(x_train, y_train)
    queries = np.array([[25], [45]], dtype=float)
    predictions = model.predict(queries)
    print("Queries:", queries.ravel().tolist())
    print("Predictions:", predictions.round(1).tolist())
    print("Training MAE (illustrative only):", round(mean_absolute_error(y_train, model.predict(x_train)), 1))


if __name__ == "__main__":
    main()
