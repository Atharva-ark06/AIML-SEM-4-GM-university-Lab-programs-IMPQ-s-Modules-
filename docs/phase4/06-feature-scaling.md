# Feature scaling

Standardization subtracts the training mean and divides by the training standard deviation. Min-max scaling maps values to a chosen interval using training-set extrema. Scaling often matters for distance-based models, gradient-based optimization, and regularized linear models; tree splits are usually less sensitive to monotonic scaling.

Fit the scaler on training data and reuse that fitted transformation for validation, test, and future inputs. Outliers can strongly affect standardization and min-max ranges.