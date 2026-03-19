#Zadatak 5

rijeci = {}

try:
    dat = open("song.txt")

    for linija in dat:
        linija = linija.lower()
        lista_rijeci = linija.split()

        for rijec in lista_rijeci:
            if rijec in rijeci:
                rijeci[rijec] += 1
            else:
                rijeci[rijec] = 1

    jednom = []

    for rijec, broj in rijeci.items():
        if broj == 1:
            jednom.append(rijec)

    print("Broj riječi koje se pojavljuju samo jednom:", len(jednom))
    print("Te riječi su:")
    for r in jednom:
        print(r)

except:
    print("Greška pri otvaranju datoteke.")