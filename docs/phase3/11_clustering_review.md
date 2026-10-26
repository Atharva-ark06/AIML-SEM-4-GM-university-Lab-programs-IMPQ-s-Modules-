# Reviewing clustering results

Clustering has no ground-truth score in many real tasks. Inspect cluster sizes, feature profiles, stability across seeds, and usefulness to the domain. Compare more than one candidate cluster count and scale features when the distance metric requires it.

Silhouette score is one diagnostic, not proof that clusters are meaningful. Document outliers and whether conclusions change under reasonable preprocessing choices.