# Probability calibration

A classifier can rank examples well while producing unreliable probabilities.

Calibration checks whether predictions near 0.8 are correct about 80% of the time over a suitable population. Reliability diagrams and Brier score are useful tools. Calibration must be learned using held-out training/validation data, never the final test set.

Calibration matters when probabilities drive decisions, thresholds, or risk estimates.