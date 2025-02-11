import numpy as np
import matplotlib.pyplot as plt
from src.preprocess import load_and_preprocess_data
from src.pca_reduction import apply_pca
from src.clustering import apply_kmeans, apply_dbscan, apply_agglomerative
from src.evaluation import evaluate_clustering
from src.visualization import plot_clusters, plot_pca_with_labels, analyze_pca_features, compare_clusters_with_labels

# Dicionário para os rótulos
label_dict = {0: 'Benigno', 1: 'Maligno'}

# Carregar e preprocessar os dados
X_scaled, y, features = load_and_preprocess_data()

# Aplicar PCA
X_pca, pca = apply_pca(X_scaled)

# Analisar a variância explicada
explained_variance = np.cumsum(pca.explained_variance_ratio_)
print(f'Variância explicada pelos primeiros componentes: {explained_variance}')

# Aplicar os algoritmos de agrupamento
kmeans_labels = apply_kmeans(X_pca)
dbscan_labels = apply_dbscan(X_pca)
agglo_labels = apply_agglomerative(X_pca)

# Avaliação dos clusters
evaluate_clustering(kmeans_labels, X_pca)
evaluate_clustering(dbscan_labels, X_pca)
evaluate_clustering(agglo_labels, X_pca)

# Visualização dos clusters e salvar imagens
plot_clusters(X_pca, kmeans_labels, 'K-Means', "kmeans.png")
plot_clusters(X_pca, dbscan_labels, 'DBSCAN', "dbscan.png")
plot_clusters(X_pca, agglo_labels, 'Agglomerative Clustering', "agglomerative.png")

# Plot dos dados reais no espaço PCA e salvar
plot_pca_with_labels(X_pca, y, "pca_labels.png")

# Comparar os clusters gerados com os rótulos verdadeiros e salvar
compare_clusters_with_labels(X_pca, y, kmeans_labels, dbscan_labels, agglo_labels, "comparison.png")

# Análise das principais features
analyze_pca_features(pca, features)

plt.show()