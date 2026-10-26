# Ensemble methods

Ensembles combine models to improve stability or predictive performance.
- Bagging trains models on resampled datasets and aggregates predictions; random forests add feature randomness.
- Boosting builds learners sequentially to focus on remaining errors.
- Voting combines different model predictions; stacking learns a second-level combination.

Compare ensembles against a simple baseline, tune only with validation data, and consider inference cost and interpretability as well as score.