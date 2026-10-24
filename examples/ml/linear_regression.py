"""Simple linear regression on a tiny synthetic dataset."""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def main():
    x = np.array([10, 20, 30, 40, 50, 60, 70, 80], dtype=float).reshape(-1, 1)
    y = np.array([120, 180, 230, 290, 340, 390, 460, 500], dtype=float)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=7)
    model = LinearRegression().fit(x_train, y_train)
    predictions = model.predict(x_test)
    print(f"Equation: y = {model.intercept_:.2f} + {model.coef_[0]:.2f}x")
    print(f"MAE={mean_absolute_error(y_test, predictions):.2f}")
    print(f"RMSE={np.sqrt(mean_squared_error(y_test, predictions)):.2f}")
    print(f"R2={r2_score(y_test, predictions):.3f}")


if __name__ == "__main__":
    main()
