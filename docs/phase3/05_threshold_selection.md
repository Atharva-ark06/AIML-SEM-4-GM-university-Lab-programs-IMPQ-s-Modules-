# Selecting a classification threshold

The default threshold of 0.5 is not universally optimal.

Choose a threshold on validation data using the task's costs, capacity limits, and desired precision or recall. Freeze the choice before final testing. Report the threshold alongside metrics because changing it changes confusion-matrix counts.

Do not tune the threshold on the test set; that makes the test result optimistic.