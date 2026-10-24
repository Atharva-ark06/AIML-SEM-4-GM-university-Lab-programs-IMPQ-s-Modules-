"""Demonstrate regression metrics on a held-out synthetic split."""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def regression_summary(actual, predicted):
    """Return named MAE, MSE, RMSE, and R2 values."""
    return {
        "mae": float(mean_absolute_error(actual, predicted)),
        "mse": float(mean_squared_error(actual, predicted)),
        "rmse": float(np.sqrt(mean_squared_error(actual, predicted))),
        "r2": float(r2_score(actual, predicted)),
    }


def main():
    x = np.arange(1, 21, dtype=float).reshape(-1, 1)
    y = 4.5 * x.ravel() + np.array([1, -2, 0, 2, -1] * 4)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=3)
    model = LinearRegression().fit(x_train, y_train)
    print(regression_summary(y_test, model.predict(x_test)))


if __name__ == "__main__":
    main()
