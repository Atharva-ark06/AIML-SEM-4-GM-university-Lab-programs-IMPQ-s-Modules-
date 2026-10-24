# Cheat sheet — supervised learning

| Algorithm | Task | Key idea | Watch out for |
|---|---|---|---|
| KNN | Classification / regression | Aggregate nearby training examples | Scaling, k choice, prediction cost |
| Linear regression | Regression | Fit a linear relationship | Outliers, nonlinearity, extrapolation |
| Decision tree | Classification / regression | Recursive feature-based splits | Overfitting, unstable splits |
| Naive Bayes | Classification | Bayes rule with conditional-independence assumption | Assumption and probability interpretation |

## Workflow
Define the target → split data → preprocess without leakage → fit → validate → evaluate once on the held-out test set → explain limitations.

No algorithm is universally best. Compare methods using the same data split and a metric appropriate to the task.
