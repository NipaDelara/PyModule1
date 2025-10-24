class Auto:
    rekisteri_tunnus =" "
    huippu_nopeus = " "
    hetkinen_nopeus = " "
    kuljettu_matka = " "

    def __init__(self, rekisteri_tunnus ,   huippu_nopeus):
        self.rekisteritunnus = rekisteri_tunnus
        self.huippunopeus = huippu_nopeus
        self.hetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def main(self):
        print("Auton tiedot:")
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Hetkinen nopeus: {self.hetkinen_nopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka} km")

uuden_auton= Auto("ABC-123",142)
uuden_auton.main()