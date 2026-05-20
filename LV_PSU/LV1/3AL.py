brojevi = []

while True:
    unos = input("Unesi broj (ili 'Done' za kraj): ")

    if unos == "Done":
        break

    try:
        broj = float(unos)
        brojevi.append(broj)
    except:
        print("To nije broj, probaj ponovo.")

if len(brojevi) > 0:
    
    brojevi.sort()
    
    koliko_ih_ima = len(brojevi)
    najmanji = min(brojevi)
    najveci = max(brojevi)
    prosjek = sum(brojevi) / koliko_ih_ima

    print("Unijeli ste ovoliko brojeva:", koliko_ih_ima)
    print("Najmanji broj:", najmanji)
    print("Najveci broj:", najveci)
    print("Prosjek:", prosjek)
    print("Sortirana lista:", brojevi)
else:
    print("Niste unijeli niti jedan broj.")