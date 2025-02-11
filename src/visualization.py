import matplotlib.pyplot as plt
import numpy as np
import os

def save_figure(fig, filename):
    os.makedirs("visualization", exist_ok=True)
    fig.savefig(f"visualization/{filename}")

def plot_clusters(X_pca, labels, title, filename=None):
    fig = plt.figure(figsize=(6, 5))
    unique_labels = set(labels)
    colors = ['r', 'b', 'g', 'y', 'c', 'm']  # Definir cores
    for label, color in zip(unique_labels, colors):
        subset = X_pca[labels == label]
        plt.scatter(subset[:, 0], subset[:, 1], c=color, label=f'Cluster {label}', alpha=0.5)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title(title)
    plt.legend()
    if filename:
        save_figure(fig, filename)
    plt.show()

def plot_pca_with_labels(X_pca, y, filename=None):
    fig = plt.figure(figsize=(6,5))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='coolwarm', alpha=0.6)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("PCA com os Rótulos Verdadeiros")
    plt.colorbar(label="0 = Benigno, 1 = Maligno")
    if filename:
        save_figure(fig, filename)
    plt.show()

def analyze_pca_features(pca, features):
    pca_components = np.abs(pca.components_)
    top_features_pc1 = [features[i] for i in np.argsort(pca_components[0])[::-1][:5]]
    top_features_pc2 = [features[i] for i in np.argsort(pca_components[1])[::-1][:5]]
    print("Principais características para separação dos clusters:")
    print(f"PC1: {top_features_pc1}")
    print(f"PC2: {top_features_pc2}")

def compare_clusters_with_labels(X_pca, y, kmeans_labels, dbscan_labels, agglo_labels, filename=None):
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    titles = ['Rótulos Verdadeiros', 'K-Means', 'DBSCAN', 'Agglomerative Clustering']
    cluster_labels = [y, kmeans_labels, dbscan_labels, agglo_labels]
    
    for ax, labels, title in zip(axes, cluster_labels, titles):
        scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='coolwarm', alpha=0.6)
        ax.set_title(title)
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
    
    plt.colorbar(scatter, ax=axes.ravel().tolist())
    if filename:
        save_figure(fig, filename)
    plt.show()