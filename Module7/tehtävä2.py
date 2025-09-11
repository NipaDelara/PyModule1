nimet = set()

while True:
    nimi = input("Annta nimi (tyhjä lopetta): ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemin syötetty nimi ")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("\nSyötetyt nimet: ")
for n in nimet:
    print(n)