lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
    print("3 = Lopeta")

    valinta = input("Anna valintasi: ")

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu!")

    elif valinta == "2":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoasema:", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")
