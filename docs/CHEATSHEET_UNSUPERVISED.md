# Cheat sheet — unsupervised learning

## Clustering
Clustering groups observations without using target labels during fitting. Cluster IDs are arbitrary labels, not rankings or ground-truth classes.

## K-means
1. Choose k initial centroids.
2. Assign each point to the nearest centroid.
3. Recalculate each centroid as the mean of its assigned points.
4. Repeat until assignments or centroids stabilize, or the iteration limit is reached.

## Important considerations
- Numeric features with different scales can distort distances.
- Different initialization can produce different results.
- Outliers can pull centroids.
- The chosen k influences the result.
- A cluster plot alone does not prove clusters are meaningful.

## Evaluation
Use domain knowledge and suitable internal or external measures. If ground-truth labels exist, keep them separate from the unsupervised fitting process.
