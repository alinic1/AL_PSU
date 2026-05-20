datoteka = open("SMSSpamCollection.txt", "r")

broj_ham_poruka = 0
suma_ham_rijeci = 0

broj_spam_poruka = 0
suma_spam_rijeci = 0
spam_sa_usklicnikom = 0

for linija in datoteka:
    rijeci = linija.split()
    
    oznaka = rijeci[0]
    
    broj_rijeci_u_poruci = len(rijeci) - 1
    
    if oznaka == "ham":
        broj_ham_poruka = broj_ham_poruka + 1
        suma_ham_rijeci = suma_ham_rijeci + broj_rijeci_u_poruci
        
    elif oznaka == "spam":
        broj_spam_poruka = broj_spam_poruka + 1
        suma_spam_rijeci = suma_spam_rijeci + broj_rijeci_u_poruci
        
        if linija.strip().endswith("!"):
            spam_sa_usklicnikom = spam_sa_usklicnikom + 1

datoteka.close()

if broj_ham_poruka > 0:
    prosjek_ham = suma_ham_rijeci / broj_ham_poruka
    print("Prosjecan broj rijeci u ham porukama:", prosjek_ham)

if broj_spam_poruka > 0:
    prosjek_spam = suma_spam_rijeci / broj_spam_poruka
    print("Prosjecan broj rijeci u spam porukama:", prosjek_spam)
    print("Broj spam poruka koje zavrsavaju usklicnikom:", spam_sa_usklicnikom)