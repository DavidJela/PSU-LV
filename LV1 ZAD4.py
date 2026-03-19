#Zadatak 4



try:
    dat = open("mbox-short.txt")

    suma = 0
    brojac = 0

    for linija in dat:
        if linija.startswith("X-DSPAM-Confidence:"):
            vrijednost = float(linija.split(":")[1])
            suma += vrijednost
            brojac += 1

    if brojac > 0:
        srednja = suma / brojac
        print("Srednja vrijednost pouzdanosti:", srednja)
    else:
        print("Nema pronađenih vrijednosti.")

except:
    print("Greška pri otvaranju datoteke.")