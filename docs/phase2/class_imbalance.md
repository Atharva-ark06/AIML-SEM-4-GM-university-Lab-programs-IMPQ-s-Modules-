# Class imbalance

Start by reporting class counts and the positive-class definition. Accuracy may look strong when a rare class is ignored.

1. Establish a baseline and inspect confusion-matrix counts.
2. Choose precision, recall, F1, PR-AUC, or cost-based metrics according to the task.
3. Tune the decision threshold on validation data, not on the final test set.
4. If resampling is justified, apply it only within training folds.
5. Compare per-class performance and document limitations.

Resampling is not automatically necessary; understand the data and deployment costs first.