# Decision-tree revision notes

Decision trees recursively split features to improve an objective such as impurity reduction. They can represent nonlinear rules and are easy to visualize, but deep trees may overfit.

Control complexity with maximum depth, minimum samples per leaf, pruning, and cross-validation. Feature importance can be biased toward features with many possible splits; use permutation importance on held-out data as a complementary check.