# K-nearest neighbours (KNN)

KNN predicts from nearby training examples under a chosen distance metric. It is simple but can be sensitive to scale, irrelevant dimensions, and the selected value of k.

Scale numeric features using training-only fitted transforms. Tune k and distance settings with validation. For classification, neighbour voting can be uniform or distance-weighted; for regression, neighbours are combined into a numeric prediction. Prediction cost can grow with training-set size.