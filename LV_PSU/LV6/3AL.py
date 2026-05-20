import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from funkcija_6_1 import generate_data

# 1. Generiraj podatke (ako već nisu u memoriji)
X = generate_data(500, flagc=1)

# 2. Izračun matrice povezivanja (linkage matrix)
# 'method' definira kako se računa udaljenost između klastera
# Opcije: 'ward', 'single', 'complete', 'average'
Z = linkage(X, method='ward')

# 3. Iscrtavanje dendrograma
plt.figure(figsize=(12, 6))
dendrogram(Z)

plt.title("Hijerarhijsko grupiranje - Dendrogram")
plt.xlabel("Indeksi uzoraka (ili broj uzoraka u zagradi)")
plt.ylabel("Udaljenost (Ward)")
plt.show()