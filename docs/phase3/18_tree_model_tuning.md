# Decision-tree tuning

Decision trees can fit nonlinear decision rules but may overfit when too deep.

Tune parameters such as maximum depth, minimum samples per leaf, and pruning using validation or cross-validation. Compare against a baseline. Tree feature importance can favor features with many split opportunities, so complement it with held-out permutation importance when useful.