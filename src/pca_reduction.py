from sklearn.decomposition import PCA
import numpy as np

def apply_pca(X_scaled, n_components=2):
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    return X_pca, pca

def analyze_pca_variance(pca):
    explained_variance = np.cumsum(pca.explained_variance_ratio_)
    print(f'Variância explicada pelos primeiros componentes: {explained_variance}')
    return explained_variance