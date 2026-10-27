# Regression metrics

- **MAE:** average absolute error; interpretable in target units and less sensitive to large errors than squared loss.
- **MSE:** average squared error; penalizes large errors more heavily and has squared target units.
- **RMSE:** square root of MSE; returns to target units.
- **R²:** compares squared error with a mean-prediction reference; it can be negative on held-out data.

No single metric captures every cost. Inspect residuals and errors in the context of the application.