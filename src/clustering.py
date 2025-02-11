from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering

def apply_kmeans(X_pca, n_clusters=2):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    return kmeans.fit_predict(X_pca)

def apply_dbscan(X_pca, eps=1.5, min_samples=5):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    return dbscan.fit_predict(X_pca)

def apply_agglomerative(X_pca, n_clusters=2):
    agglo = AgglomerativeClustering(n_clusters=n_clusters)
    return agglo.fit_predict(X_pca)