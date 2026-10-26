# Baselines before complex models

A baseline answers: Does the candidate improve on a simple, defensible reference?

For classification, try a majority-class or DummyClassifier baseline. For regression, try a mean/median predictor or DummyRegressor. Then compare using the same folds and metrics as the candidate.

Report the baseline score, candidate score, data split, and metric definition. A high score alone does not prove the model is useful, fair, or reliable.