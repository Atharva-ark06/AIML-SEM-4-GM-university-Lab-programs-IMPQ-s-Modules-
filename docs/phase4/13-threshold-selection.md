# Choosing a classification threshold

A probability model often predicts the positive class when its score exceeds a threshold. The default 0.5 is a convention, not a law. Lower thresholds usually increase recall and may increase false positives; higher thresholds usually reduce false positives and may miss more positives.

Choose thresholds using validation data and a stated cost or operating constraint. Do not tune a threshold on the final test set. Re-check calibration and operating characteristics when the data distribution changes.