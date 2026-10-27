# Class imbalance

Accuracy can be misleading when one class dominates. Report precision, recall, F1, and a confusion matrix where appropriate; consider PR-AUC for rare positive classes. Select the positive class explicitly.

Resampling or class weights must be applied within training folds only. Never oversample before splitting, because near-duplicate examples can leak across partitions. Choose thresholds based on validation data and the relative costs of false positives and false negatives.