# Cheat sheet — model evaluation metrics

## Classification
- **Accuracy:** correct predictions divided by all predictions.
- **Precision:** TP / (TP + FP); among predicted positives, how many were correct?
- **Recall / sensitivity:** TP / (TP + FN); among actual positives, how many were found?
- **Specificity:** TN / (TN + FP).
- **F1:** harmonic mean of precision and recall.

When classes are imbalanced, accuracy alone can hide poor performance on the minority class. Always state which class is considered positive.

## Regression
- **MAE:** mean absolute error; less sensitive to large errors than squared-error metrics.
- **MSE:** mean squared error; penalizes large errors more strongly.
- **RMSE:** square root of MSE; same units as the target.
- **R²:** relative fit measure against a mean-prediction baseline; can be negative on held-out data.

## Evaluation hygiene
Evaluate the final model on data not used for fitting or parameter selection. Do not choose the model based on repeated inspection of the test set.
