import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
import sys

# 1. Učitavanje slike u boji
try:
    img = mpimg.imread('example.png') # Pripazi je li .png ili .jpg
except FileNotFoundError:
    print("Greška: Datoteka nije pronađena!")
    sys.exit()

# Normalizacija na 0-1 za stabilnost KMeans algoritma
if img.max() > 1.0:
    img = img / 255.0

# Ako slika ima Alpha kanal (RGBA), mičemo ga za KMeans
if img.shape[2] == 4:
    img = img[:, :, :3]

# 2. Transformacija slike u niz piksela (n_samples, n_features)
w, h, d = img.shape
X = img.reshape((w * h, d))

# 3. Primjena K-means algoritma
n_colors = 8
kmeans = KMeans(n_clusters=n_colors, n_init='auto', random_state=42)
labels = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

# 4. Rekonstrukcija kvantizirane slike
# Osiguravamo da su vrijednosti u rasponu [0, 1] pomoću np.clip
quantized_img = centers[labels].reshape((w, h, d))
quantized_img = np.clip(quantized_img, 0, 1)

# 5. Prikaz rezultata
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Originalna slika')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(quantized_img)
plt.title(f'Kvantizirana slika ({n_colors} boja)')
plt.axis('off')

plt.tight_layout()
plt.show()