# Feature engineering

Feature engineering converts raw fields into inputs a model can use.

Examples include extracting month from a date, computing ratios with safe zero handling, and grouping rare categories when justified. Fit learned transformations on training data only, then apply the fitted transformation unchanged to validation and test data.

Document why each feature is available at prediction time. A feature that leaks future information can create misleadingly high scores.