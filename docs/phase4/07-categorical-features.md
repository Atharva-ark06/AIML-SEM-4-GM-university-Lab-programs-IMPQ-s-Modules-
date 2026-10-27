# Categorical feature handling

Nominal categories have no inherent order; one-hot encoding is a common representation. Ordinal categories have meaningful order and may need an explicitly defined mapping. Never assign arbitrary integer codes to nominal categories and then assume the numeric distances are meaningful.

Handle unseen categories deliberately, and fit encoders on training data. For high-cardinality columns, assess memory, rare-category behavior, and whether the feature is actually available at prediction time.