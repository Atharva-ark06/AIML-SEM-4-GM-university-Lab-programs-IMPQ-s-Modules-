# Data-quality checklist

Before modelling, check:
- **Shape:** expected number of rows and columns.
- **Schema:** numeric, categorical, date, and target types.
- **Missingness:** count and percentage per column; consider whether absence is informative.
- **Duplicates:** identify exact duplicate rows and repeated entity identifiers.
- **Ranges:** flag impossible values using domain rules rather than arbitrary assumptions.
- **Labels:** inspect class balance and inconsistent spellings.
- **Provenance:** note source, collection time, licensing, and known limitations.

A quality report should flag issues for review; it should not silently delete records or overwrite source data.