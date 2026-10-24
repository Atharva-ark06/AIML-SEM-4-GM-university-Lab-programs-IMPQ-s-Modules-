# Module 3 — similarity-based learning

## Main idea
Similarity-based methods predict an output by comparing a new example with stored examples. K-Nearest Neighbors (KNN) is a common instance.

## KNN workflow
1. Choose features and a distance metric.
2. Prepare features on comparable scales when needed.
3. Select a value for k.
4. Find the k nearest training examples.
5. For classification, vote among their labels; for regression, aggregate their numeric targets.
6. Evaluate predictions on data not used to fit or tune the model.

## Euclidean distance
For vectors (x) and (y), Euclidean distance is (sqrt{sum_i (x_i-y_i)^2}). Features with large numeric ranges can dominate this distance, so scaling is often important.

## Choosing k
A very small k may be sensitive to noise; a very large k may smooth away local structure. Select k using a validation procedure rather than the test set.

## Strengths and limitations
- Simple and intuitive.
- No explicit parametric training stage.
- Prediction can be expensive for large datasets.
- Sensitive to feature representation, scaling, distance metric, and irrelevant dimensions.

## Revision prompts
Explain KNN by tracing one query point, and discuss why scaling and train/test separation matter.
