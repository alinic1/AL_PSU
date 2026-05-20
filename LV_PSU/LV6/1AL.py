import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from funkcija_6_1 import generate_data

# Generiranje 500 podataka (promijeni flagc od 1 do 5 za razne oblike)
X = generate_data(500, flagc=1)

# Inicijalizacija i učenje K-means modela
# Uzimamo npr. 3 klastera
n_clusters = 3
km = KMeans(n_clusters=n_clusters, init='random', n_init=10)
km.fit(X)

# Predviđanje pripadnosti klasterima
labels = km.predict(X)
centers = km.cluster_centers_

# Vizualizacija
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centar')
plt.title(f"K-means grupiranje (K={n_clusters})")
plt.legend()
plt.show()