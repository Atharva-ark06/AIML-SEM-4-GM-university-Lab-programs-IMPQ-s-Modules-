# Data leakage

Data leakage occurs when information unavailable at prediction time influences training or evaluation. Examples include scaling the full dataset before splitting, using a future outcome as a feature, or allowing records from the same person to appear in both train and test when the intended use is new people.

**Prevention:** split first; fit preprocessing on training data; use pipelines; define time/group boundaries that match deployment; keep the final test set untouched during tuning. Suspiciously high scores should trigger a leakage audit rather than immediate celebration.