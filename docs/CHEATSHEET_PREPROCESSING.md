# Cheat sheet — data preprocessing

1. Inspect row count, column types, ranges, duplicates, and missing values.
2. Separate target from input features.
3. Split into train and test sets before learning preprocessing statistics.
4. Fit imputers, encoders, and scalers on training data only.
5. Transform the test data with the fitted training transformers.
6. Train a baseline model.
7. Evaluate and document assumptions.

## Common operations
- **Missing values:** remove rows only when justified, or impute with a training-set statistic / model.
- **Categorical encoding:** one-hot encode nominal categories; ordinal encoding is appropriate only when an order is meaningful.
- **Min-max scaling:** maps training feature range to a chosen interval, often [0, 1].
- **Standardization:** subtract training mean and divide by training standard deviation.
- **Robust scaling:** uses median and interquartile range, reducing sensitivity to extreme values.

## Leakage warning
Fitting a scaler on the entire dataset before splitting leaks information from test data into preprocessing. Use a pipeline when possible.
