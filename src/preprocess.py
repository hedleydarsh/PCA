import pandas as pd
import os
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(save_csv=True):
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    X = df.drop(columns=['target'])
    y = df['target']
    features = data.feature_names
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Salvar os dados em CSV na pasta data/
    if save_csv:
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/breast_cancer.csv", index=False)
    
    return X_scaled, y, features