"""K-means clustering example using generated two-dimensional data."""
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler


def main():
    x, _hidden_labels = make_blobs(n_samples=120, centers=3, random_state=10, cluster_std=1.2)
    x_scaled = StandardScaler().fit_transform(x)
    model = KMeans(n_clusters=3, random_state=10, n_init=10)
    labels = model.fit_predict(x_scaled)
    print("Cluster counts:", {int(label): int((labels == label).sum()) for label in set(labels)})
    print("Note: generated labels are arbitrary cluster IDs, not class names.")


if __name__ == "__main__":
    main()
