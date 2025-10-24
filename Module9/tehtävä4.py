import random

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

    def kulje(self, tunnit):
        self.kuljettu_matka += self.hetkinen_nopeus * tunnit

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteri_tunnus}")
        print(f"Huippunopeus: {self.huippu_nopeus} km/h")
        print(f"Hetkinen nopeus: {self.hetkinen_nopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka:.1f} km")

def main():
    # Luodaan lista
    autot = []
    for i in range(1, 11):
        huippu_nopeus = random.randint(100, 200)
        rekisteri_tunnus = f"ABC-{i}"
        autot.append(Auto(rekisteri_tunnus, huippu_nopeus))

    # Aloitetaan kilpailu
    kilpailu_kaynnissa = True
    tunnit = 0

    while kilpailu_kaynnissa:
        tunnit += 1
        for auto in autot:
            nopeus_muutos = random.randint(-10, 15)  # arvotaan nopeuden muutos
            auto.kiihdyta(nopeus_muutos)
            auto.kulje(1)  # ajetaan yksi tunti

            if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False
                break

    # Tulos lopputulokset
    print(f"\nKilpailu päättyi {tunnit} tunnin jälkeen!\n")
    print(f"{'Rekisteritunnus':<12} {'Huippunopeus':<13} {'Nopeus':<10} {'Matka (km)':<12}")
    print("-" * 50)
    for auto in autot:
        print(f"{auto.rekisteri_tunnus:<12} {auto.huippu_nopeus:<13} {auto.hetkinen_nopeus:<10} {auto.kuljettu_matka:<12.1f}")

if __name__ == "__main__":
    main()
