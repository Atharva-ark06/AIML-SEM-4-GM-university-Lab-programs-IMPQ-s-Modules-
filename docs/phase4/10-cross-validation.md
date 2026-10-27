# Cross-validation

K-fold cross-validation partitions training data into folds, repeatedly fitting on some folds and validating on the remaining fold. It provides a more stable estimate than one small split when its assumptions fit the data.

Use stratified folds for many classification tasks, group-aware folds for related records, and time-aware validation for temporal tasks. Keep the final test set outside model selection. Report fold variability, not just the best score.