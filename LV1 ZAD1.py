#Zadatak 1


def total_euro(sati, cijena_po_satu):
    return sati * cijena_po_satu


sati = float(input("Unesite broj radnih sati: "))
cijena_po_satu = float(input("Unesite koliko ste plaćeni po satu: "))

zarada = total_euro(sati, cijena_po_satu)

print("Ukupno ste zaradili:", zarada, "eura")