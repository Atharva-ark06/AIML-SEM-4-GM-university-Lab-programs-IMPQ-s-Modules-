# Handling imbalanced classes

Begin with class counts and a simple baseline. Accuracy alone can conceal poor minority-class recall. Consider precision, recall, F1, PR-AUC, and the costs of each error.

If resampling or class weighting is appropriate, apply it only to training data or within each training fold. Keep validation and test distributions untouched and report per-class results.