rjecnik = {}

datoteka = open("song.txt", "r")

for linija in datoteka:
    rijeci = linija.lower().split()
    
    for rijec in rijeci:
        rijec = rijec.strip(".,!?:;")
        
        if rijec in rjecnik:
            rjecnik[rijec] = rjecnik[rijec] + 1
        else:
            rjecnik[rijec] = 1

datoteka.close()

jedinstvene_broj = 0

print("Rijeci koje se pojavljuju samo jednom u datoteci:")

for rijec in rjecnik:
    if rjecnik[rijec] == 1:
        print(rijec)
        jedinstvene_broj = jedinstvene_broj + 1
        
print("Ukupno rijeci koje se pojavljuju samo jednom:", jedinstvene_broj)