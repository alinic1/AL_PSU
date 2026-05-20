ime_datoteke = input("Unesite ime datoteke: ")

try:
    datoteka = open(ime_datoteke, 'r')
    
    suma = 0.0
    brojac = 0
    
    for linija in datoteka:
        if linija.startswith("X-DSPAM-Confidence:"):
            
            dijelovi = linija.split()
            
            vrijednost = float(dijelovi[1])
            
            suma = suma + vrijednost
            brojac = brojac + 1
            
    if brojac > 0:
        prosjek = suma / brojac
        print(f"Average X-DSPAM-Confidence: {prosjek}")
    else:
        print("U datoteci nije pronađena niti jedna linija s pouzdanošću.")

    datoteka.close()

except FileNotFoundError:
    print(f"Greška: Datoteka '{ime_datoteke}' ne postoji.")