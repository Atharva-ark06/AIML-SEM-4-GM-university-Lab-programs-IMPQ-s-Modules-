# Encoding categorical features

- One-hot encoding represents nominal categories with indicator columns.
- Ordinal encoding is appropriate only when a meaningful order exists.
- Unknown categories at inference time should be handled intentionally.
- High-cardinality identifiers may cause overfitting and should be examined carefully.

Keep encoders inside a training pipeline. Do not assign arbitrary numeric order to unordered labels, and do not treat a record ID as a meaningful predictor without justification.