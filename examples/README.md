# Runnable examples

These examples are small teaching demonstrations. They supplement the existing course files and are not replacements for official lab instructions.

## Run
From the repository root, install `requirements.txt`, then run a file with Python. Example:

```bash
python examples/search/bfs.py
python examples/search/astar.py
python examples/ml/knn_classification.py
python examples/ml/kmeans_clustering.py
```

## Search examples
- `search/bfs.py`: shortest path by edge count in an unweighted graph.
- `search/dfs.py`: depth-first graph traversal and path discovery.
- `search/astar.py`: lowest-cost path with a heuristic.
- `search/ao_star.py`: compact acyclic AND-OR cost example.

## ML examples
Examples cover scaling, train/test splitting, encoding, missing values, KNN, regression, decision trees, Naive Bayes, K-means, evaluation metrics, cross-validation, and pipelines.

Each file includes a main guard so it can be imported without running its demonstration. Results on tiny synthetic data are illustrative and should not be interpreted as scientific evidence.
