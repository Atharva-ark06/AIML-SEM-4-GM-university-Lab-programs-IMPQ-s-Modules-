# High-cardinality categorical features

A category with many distinct values can create sparse representations and overfitting risk.

Check whether a field is an identifier, whether categories recur, and whether unseen categories are expected. Use a deliberate strategy such as one-hot encoding for manageable cardinality, grouping rare values, or a validated alternative. Avoid arbitrary numeric ordering for nominal categories.