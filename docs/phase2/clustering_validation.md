# Validating clusters

Clustering has no single universally correct score. Use several checks:
- Inspect cluster sizes and feature profiles.
- Compare silhouette score when its assumptions fit the metric and data.
- Consider inertia for K-means, remembering it decreases as cluster count increases.
- Test stability across random seeds or samples.
- Ask whether the segments are useful for the intended decision.

Do not choose a cluster count from one score alone or interpret clusters as natural categories without domain evidence.