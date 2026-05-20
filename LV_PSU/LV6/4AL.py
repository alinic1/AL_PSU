import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from sklearn import cluster

# 1. Učitavanje slike [cite: 75, 76]
img_gray = mpimg.imread('example_grayscale.png')

# 2. Priprema podataka
# K-means treba (n_samples, n_features). Za grayscale to je (pikseli, 1) [cite: 118]
X = img_gray.reshape((-1, 1))

# 3. Primjena K-means algoritma
k = 10 # Broj klastera (nijansi) 
k_means = cluster.KMeans(n_clusters=k, n_init=1)
k_means.fit(X)

# 4. Rekonstrukcija slike
values = k_means.cluster_centers_.squeeze() # Centri klastera (intenziteti sive) [cite: 121]
labels = k_means.labels_ # Pripadnost svakog piksela klasteru [cite: 122]

# Zamjena originalnih piksela centrima klastera
face_compressed = values[labels].reshape(img_gray.shape)

# 5. Prikaz [cite: 125, 126, 127, 128]
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap='gray')
plt.title("Originalna slika")
plt.subplot(1, 2, 2)
plt.imshow(face_compressed, cmap='gray')
plt.title(f"Kvantizirana slika (K={k})")
plt.show()