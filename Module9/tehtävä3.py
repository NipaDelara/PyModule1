class Auto :
    def __init__(self, rekisteri_tunnus, huippu_nopeus):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippu_nopeus = huippu_nopeus
        self.hetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self,  nopeus_muutos):
        self.hetkinen_nopeus += nopeus_muutos

        if self.hetkinen_nopeus > self.huippu_nopeus:
            self.hetkinen_nopeus = self.huippu_nopeus

        if self.hetkinen_nopeus < 0:
            self.hetkinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.hetkinen_nopeus * tunnit


    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteri_tunnus}")
        print(f"Huippunopeus: {self.huippu_nopeus} km/h")
        print(f"Hetkinen nopeus: {self.hetkinen_nopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka:.1f} km")

def main():
    uuden_auton= Auto("ABC-123",142)

    #Kiihdytä autoa
    uuden_auton.kiihdyta(60)
    print("\nKiihdytyksen jälkeen: ")

    uuden_auton.tulosta_tiedot()

    #1.5 tuntia aja
    uuden_auton.kulje(1.5)
    print("\nAjettu 1.5 tuntia:")
    uuden_auton.tulosta_tiedot()

    #kiihdytä lisää ja aja uudesta
    uuden_auton.kiihdyta(40)
    uuden_auton.kulje(2)
    print("\nLisäkiihdytyksen ja ajon jälkeen:")

    uuden_auton.tulosta_tiedot()

if __name__ == "__main__":
    main()