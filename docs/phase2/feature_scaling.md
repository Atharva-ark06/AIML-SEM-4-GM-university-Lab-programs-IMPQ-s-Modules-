# Feature scaling

Scaling can help distance-based and gradient-based algorithms, including KNN, K-means, and many linear models.

- Min-max scaling maps values to a selected range and is sensitive to outliers.
- Standardization centers values and scales by standard deviation.
- Robust scaling uses median and interquartile range and can be less sensitive to outliers.
- Tree-based models often need little or no scaling.

Fit the scaler on training data only. Scaling does not make features normally distributed and does not remove outliers.