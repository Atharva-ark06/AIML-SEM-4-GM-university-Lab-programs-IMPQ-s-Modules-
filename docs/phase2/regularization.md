# Regularization

Regularization discourages overly complex parameter values and can improve generalization.
- L1 penalty can drive some coefficients to zero.
- L2 penalty shrinks coefficients smoothly.
- Elastic Net combines L1 and L2 penalties.

The strength of regularization is a hyperparameter and must be selected on training/validation data. Standardize features when coefficient penalties should be comparable across different measurement scales.