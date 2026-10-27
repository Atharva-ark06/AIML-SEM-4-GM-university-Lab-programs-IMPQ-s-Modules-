# Classification metrics

Precision = TP / (TP + FP); recall = TP / (TP + FN); F1 is the harmonic mean of precision and recall. Accuracy is the fraction of correct predictions. These metrics answer different questions and depend on the selected positive class.

Always state the averaging method for multiclass precision/recall/F1. A confusion matrix exposes the types of mistakes. If a denominator is zero, code should define a documented zero-division policy rather than crash silently.