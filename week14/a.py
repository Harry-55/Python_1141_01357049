import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

iris = load_iris()
df = pd.DataFrame(
    data=iris.data,
    columns=iris.feature_names
)
df['target'] = iris.target
df['species'] = df['target'].map(
    {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[iris.feature_names])

kmeans = KMeans(n_clusters=3, random_state=350234, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)
# print(df.head())
for c in sorted(df['cluster'].unique()):
    most_common_species = (
        df[df['cluster'] == c]['species']
        .value_counts()
        .idxmax()
    )
    print(f"Cluster {c}: {most_common_species}")



