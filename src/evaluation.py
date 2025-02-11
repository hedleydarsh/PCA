from sklearn.metrics import silhouette_score, davies_bouldin_score

def evaluate_clustering(labels, X):
    if len(set(labels)) > 1:
        silhouette = silhouette_score(X, labels)
        db_index = davies_bouldin_score(X, labels)
        print(f'Silhouette Score: {silhouette:.4f}, Davies-Bouldin Index: {db_index:.4f}')
    else:
        print('Somente um cluster encontrado. Avaliação não possível.')