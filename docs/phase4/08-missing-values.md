# Missing-value analysis

Missingness can be caused by measurement failure, skipped questions, system behavior, or the value being inapplicable. Count missing values by column and inspect whether missingness varies across time or groups.

Simple numeric median and categorical most-frequent imputation are useful baselines, not universal truths. Fit imputation values on training data only. Add a missingness indicator only when it is defensible and available at prediction time; document assumptions.