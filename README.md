# 📌 Projeto: Machine Machine Learning II - Aprendizado Não-Supervisionado com PCA e Clustering

Este projeto foi desenvolvido como parte da disciplina de **Aprendizado Não-Supervisionado** do curso de **Pós-Graduação em Análise de Dados e Inteligência Artificial da UFMA**. O objetivo é aplicar técnicas de **redução de dimensionalidade** e **agrupamento de dados** para analisar um conjunto de dados de câncer de mama.

---

## 🎯 **Objetivo do Projeto**

O projeto utiliza **aprendizado não-supervisionado** para identificar padrões no conjunto de dados **Breast Cancer Wisconsin**. Para isso, foram aplicadas as seguintes técnicas:

✅ **Redução de dimensionalidade com PCA** (Principal Component Analysis) para representar os dados em um espaço de menor dimensão sem perder muita informação.  
✅ **Algoritmos de agrupamento (clustering)** para identificar padrões sem utilizar rótulos:

- **K-Means**
- **DBSCAN**
- **Agglomerative Clustering**
  ✅ **Avaliação dos clusters gerados** utilizando métricas como **Silhouette Score** e **Davies-Bouldin Index**.  
  ✅ **Visualização dos agrupamentos gerados e comparação com os rótulos verdadeiros** para verificar a qualidade das segmentações.

---

## 📂 **Estrutura do Projeto**

O projeto está organizado da seguinte forma:

```
Breast_Cancer_Clustering/
│── data/
│   ├── breast_cancer.csv  # Base de dados pré-processada
│── src/
│   ├── preprocess.py  # Carrega e processa os dados
│   ├── pca_reduction.py  # Aplica PCA
│   ├── clustering.py  # Algoritmos de agrupamento
│   ├── evaluation.py  # Avaliação dos clusters
│   ├── visualization.py  # Geração de gráficos e visualizações
│── visualization/
│   ├── comparison.png  # Comparação dos clusters gerados com os rótulos verdadeiros
│   ├── kmeans.png  # Visualização do agrupamento K-Means
│   ├── dbscan.png  # Visualização do agrupamento DBSCAN
│   ├── agglomerative.png  # Visualização do agrupamento hierárquico
│── main.py  # Arquivo principal que executa o fluxo completo
│── requirements.txt  # Dependências do projeto
│── README.md  # Documentação do projeto
```

---

## 🚀 **Como Clonar e Executar o Projeto**

### 🔹 **1. Clonar o Repositório**

Para obter uma cópia local do projeto, execute o seguinte comando no terminal:

```bash
git clone https://github.com/hedleydarsh/PCA.git
cd PCA
```

### 🔹 **2. Instalar as Dependências**

Antes de executar o projeto, instale as bibliotecas necessárias utilizando o `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 🔹 **3. Executar o Código Principal**

Para rodar o fluxo completo de **pré-processamento, PCA, clustering, avaliação e visualização**, execute:

```bash
python main.py
```

Após a execução, os resultados serão gerados na pasta `visualization/` e os dados processados serão salvos em `data/breast_cancer.csv`.

---

## 📊 **Resultados Obtidos**

### 🔹 **Redução de Dimensionalidade (PCA)**

- O PCA conseguiu representar **63,24% da variância total** dos dados com apenas **dois componentes principais**.
- As características mais relevantes identificadas foram **concavidade, perímetro e dimensão fractal**.

### 🔹 **Qualidade dos Agrupamentos**

- **K-Means e Agglomerative Clustering** foram os métodos que melhor capturaram a separação entre tumores benignos e malignos.
- **DBSCAN não conseguiu formar clusters bem definidos**, pois muitos pontos foram tratados como ruído.

### 🔹 **Visualizações dos Clusters**

- As imagens geradas mostram que **os clusters não são perfeitamente separados**, o que indica que **PCA e clustering não são suficientes para uma classificação precisa**.
- O próximo passo poderia ser testar um **modelo supervisionado** para melhorar a classificação dos tumores.

---

## 🏆 **Conclusão**

📌 Este projeto demonstrou como o **aprendizado não-supervisionado** pode ser utilizado para identificar padrões em **dados médicos**, mesmo sem rótulos.  
📌 Apesar de o PCA e os algoritmos de clustering conseguirem capturar **tendências nos dados**, a sobreposição dos grupos indica que **um modelo supervisionado seria mais eficiente para diagnosticar tumores**.  
📌 A abordagem permitiu compreender quais características são mais relevantes para a separação entre **tumores benignos e malignos**, auxiliando no desenvolvimento de futuras análises preditivas.

---

## ✉ **Contato**

Caso tenha dúvidas ou sugestões, sinta-se à vontade para entrar em contato!
