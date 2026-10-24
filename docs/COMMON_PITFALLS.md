# Common AIML coding and exam pitfalls

- **Confusing AI with ML:** ML is one approach within the broader field of AI.
- **Using DFS for a shortest path:** DFS finds a path but not necessarily the shortest one.
- **Ignoring visited states:** graph search can revisit nodes or loop on cycles.
- **Using a bad heuristic:** an overestimating heuristic can break A* optimality guarantees.
- **Scaling before splitting:** this can leak information from the test set.
- **Scaling only the training set manually:** fit on training data and apply the same transformer to test data.
- **Choosing k from the test set:** use validation or cross-validation.
- **Reporting only accuracy:** inspect class balance and additional metrics.
- **Confusing clustering and classification:** clustering does not learn from class labels during fitting.
- **Treating R² as always between 0 and 1:** held-out R² can be negative.
- **Using tiny synthetic data for broad conclusions:** it is suitable for learning code flow, not for strong claims.
- **Assuming every legacy script runs in every environment:** inspect imports, paths, and interactive behaviour first.
