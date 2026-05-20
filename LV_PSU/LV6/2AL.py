import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from funkcija_6_1 import generate_data

# 1. Generiraj podatke (nemoj zaboraviti ovaj korak!)
X = generate_data(500, flagc=1)

# 2. Lista u koju spremamo vrijednosti J (inercije)
inercija = []
K_raspon = range(1, 21) # Broj klastera od 1 do 20 [cite: 63]

for k in K_raspon:
    # Inicijalizacija KMeans za trenutni k
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    
    # Treniranje na podacima X
    km.fit(X)
    
    # Dohvaćanje vrijednosti kriterijske funkcije (inercije) [cite: 63]
    inercija.append(km.inertia_)

# 3. Prikaz rezultata na grafu [cite: 63]
plt.figure(figsize=(10, 6))
plt.plot(K_raspon, inercija, marker='o', linestyle='--')
plt.xlabel('Broj klastera (K)')
plt.ylabel('Vrijednost kriterijske funkcije (J)')
plt.title('Metoda lakta (Elbow Method)')
plt.xticks(K_raspon) # Prikazuje sve brojeve od 1 do 20 na x-osi
plt.grid(True)
plt.show()