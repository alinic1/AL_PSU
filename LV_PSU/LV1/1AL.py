radni_sat = float(input("Unesite broj radnih sati: "))
satnica = float(input("Unesite satnicu: "))

zarada = radni_sat * satnica

#print("Korisnik je zaradio: ", zarada, " eura")

def total_euro(radni_sat, satnica):
    ukupna_zarada = radni_sat * satnica
    return ukupna_zarada

rezultat = total_euro(radni_sat, satnica)

print("Ukupna zarada iznosi: ", rezultat, " eura")


