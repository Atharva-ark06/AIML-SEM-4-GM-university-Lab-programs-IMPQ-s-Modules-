# Principal component analysis (PCA)

PCA creates orthogonal directions that capture decreasing amounts of variance. It is commonly used for dimensionality reduction and visualization of numeric data.

Workflow: handle missing values, scale features when units differ, fit PCA on training data, inspect explained variance, and transform held-out data using the fitted object. Principal components are combinations of original variables and may be harder to interpret. PCA preserves variance, not necessarily class separation.