# Choosing a data split

- **Random split:** appropriate when rows are independent and exchangeable.
- **Stratified split:** preserves approximate class proportions for classification.
- **Group split:** keeps related entities (such as a person or device) in one partition.
- **Time-based split:** trains on the past and evaluates on later observations.

Choose the split to simulate how the model will be used. A random split is not automatically valid for longitudinal, grouped, or time-dependent data.