# A repeatable machine-learning workflow

1. State the question and target variable.
2. Inspect row count, column types, duplicates, missing values, and label balance.
3. Split data before fitting any transform that learns from data.
4. Build preprocessing and estimator steps in a pipeline.
5. Choose metrics that match the task and error costs.
6. Compare a simple baseline with candidate models using the same validation strategy.
7. Evaluate once on a held-out test set.
8. Record the seed, parameters, metrics, limitations, and data provenance.

## Common leakage warning
Do not scale, impute, select features, or oversample the entire dataset before splitting. Fit such steps on training folds only.