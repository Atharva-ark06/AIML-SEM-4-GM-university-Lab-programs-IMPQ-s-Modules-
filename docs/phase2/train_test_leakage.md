# Train/test leakage

Leakage occurs when information unavailable at prediction time influences training or model selection.

Examples:
- Scaling the full dataset before splitting.
- Using a post-outcome field to predict an earlier outcome.
- Selecting features using all labels before cross-validation.
- Letting rows from the same person appear in both train and test when person-level independence matters.

## Prevention
Split first; put learned preprocessing inside a pipeline; group or time-split when the data-generating process requires it; keep the final test set untouched until model selection is complete.