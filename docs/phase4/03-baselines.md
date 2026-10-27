# Why establish a baseline?

A baseline is a deliberately simple reference that makes later results interpretable. For classification, common baselines predict the most frequent training label. For regression, predict the training-set mean or median.

A complex model that cannot beat a reasonable baseline may indicate weak features, data leakage in an earlier comparison, an unsuitable metric, or a task with little learnable signal. Compute the baseline using training data only and evaluate it on the same held-out examples as candidate models.