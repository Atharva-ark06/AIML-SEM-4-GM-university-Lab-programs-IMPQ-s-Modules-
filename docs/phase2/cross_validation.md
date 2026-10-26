# Cross-validation notes

K-fold cross-validation rotates held-out folds and estimates performance more robustly than a single small validation split.

- Use stratified folds for imbalanced classification where appropriate.
- Use group-aware splitting when records from one subject/device must not cross folds.
- Use time-aware splitting when future observations must not influence past predictions.
- Fit preprocessing separately inside each training fold, ideally through a pipeline.
- Report mean and variability; do not treat folds as independent experiments.

Cross-validation is a design choice, not a cure for biased or unrepresentative data.