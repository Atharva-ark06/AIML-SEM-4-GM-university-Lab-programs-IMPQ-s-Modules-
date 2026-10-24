# Module 4 — regression and decision trees

## Regression
Regression predicts a continuous numerical target. In simple linear regression, the model is (\hat{y}=\beta_0+\beta_1x), where the intercept is the predicted value at x = 0 and the slope describes the predicted change per unit of x.

## Least-squares intuition
Ordinary least squares chooses coefficients to minimize the sum of squared residuals on the training data. A fitted line describes an association in the data; it does not by itself prove causation.

## Decision trees
A decision tree recursively partitions data using feature-based rules. Classification trees predict categories; regression trees predict numeric values. Deep trees can memorize training patterns and overfit.

## Evaluation
- **MAE:** average absolute prediction error.
- **MSE:** average squared error.
- **RMSE:** square root of MSE, expressed in the target's units.
- **R²:** compares model residual variation with a baseline based on the target mean; it can be negative on test data.

## Practical checklist
- Separate training and test data.
- Fit preprocessing only on training data.
- Compare against a simple baseline.
- Inspect residuals and metric context.
- Avoid claiming a model is good from one metric alone.
