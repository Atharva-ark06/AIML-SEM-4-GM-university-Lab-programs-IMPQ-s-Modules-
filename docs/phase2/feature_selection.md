# Feature selection

Feature selection reduces input dimensions and may improve interpretability, cost, or generalization. Common approaches include:
- Filter methods: rank features using statistics independent of a particular estimator.
- Wrapper methods: evaluate subsets using a model and validation process.
- Embedded methods: select features during model fitting, such as regularized linear models or tree-based importance.

Perform selection inside cross-validation folds. Correlation or importance is not proof of causation, and selection stability should be checked when data are small.