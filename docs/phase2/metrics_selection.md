# Choosing evaluation metrics

## Classification
- Accuracy: overall fraction correct; can hide minority-class failure.
- Precision: among predicted positives, fraction truly positive.
- Recall: among actual positives, fraction detected.
- F1: harmonic mean of precision and recall.
- ROC-AUC: ranking quality across thresholds; inspect precision-recall curves for rare positives.

## Regression
- MAE: average absolute error in target units.
- MSE/RMSE: penalize large errors more strongly.
- R²: relative fit against a mean baseline; can be negative on held-out data.

Choose metrics from the task's error costs, not because a metric is popular.