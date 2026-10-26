# Model interpretability

Interpretability helps explain model behavior but does not prove causation.

Start with a simple baseline and inspect feature distributions, errors, and stability. Permutation importance measures how a score changes when a feature is shuffled, but correlated features can share or mask importance. Explain local predictions carefully and state the population and dataset version to which an explanation applies.