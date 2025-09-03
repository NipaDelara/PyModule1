oikea_tunnus ="python"
oikea_salasana = "rules"

yrittää = 0

while yrittää < 5:
    tunnus = input("Anna kyttajatunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana== oikea_salasana :
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana")
        yrittää += 1
if yrittää ==5:
    print("pääsy evätty")



