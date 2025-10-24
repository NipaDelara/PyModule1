class Auto:
    def __init__(self, rekisteri_tunnus, huippu_nopeus):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippu_nopeus = huippu_nopeus
        self.hetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeus_muutos):
        self.hetkinen_nopeus += nopeus_muutos

        if self.hetkinen_nopeus > self.huippu_nopeus:
            self.hetkinen_nopeus = self.huippu_nopeus

        if self.hetkinen_nopeus < 0:
            self.hetkinen_nopeus = 0

    def main(self):
        print("Auton tiedot:")
        print(f"Rekisteritunnus: {self.rekisteri_tunnus}")
        print(f"Huippunopeus: {self.huippu_nopeus} km/h")
        print(f"Hetkinen nopeus: {self.hetkinen_nopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka} km")


uuden_auton = Auto("ABC-123", 142)
uuden_auton.main()

uuden_auton.kiihdyta(30)
uuden_auton.kiihdyta(70)
uuden_auton.kiihdyta(50)

print("\nKiihdytysten jälkeen:")
print(f"Auton nopeus: {uuden_auton.hetkinen_nopeus} km/h")

uuden_auton.kiihdyta(-200)
print("\nHätäjarrutuksen jälkeen:")
print(f"Auton nopeus: {uuden_auton.hetkinen_nopeus} km/h")