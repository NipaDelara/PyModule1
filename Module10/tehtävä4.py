import random

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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeus_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeus_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteri':<10}{'Huippu':<10}{'Nopeus':<10}{'Matka (km)':<12}")
        print("-" * 42)
        for auto in self.autot:
            print(f"{auto.rekisteri_tunnus:<10}{auto.huippu_nopeus:<10}{auto.hetkinen_nopeus:<10}{auto.kuljettu_matka:<12.1f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


def main():
    # 10 autot
    autot = []
    for i in range(1, 11):
        rekisteri_tunnus = f"ABC-{i}"
        huippu_nopeus = random.randint(100, 200)
        autot.append(Auto(rekisteri_tunnus, huippu_nopeus))

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
    tunnit = 0

    print(f"Kilpailu '{kilpailu.nimi}' alkaa!\n")
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1

        if tunnit % 10 == 0:
            print(f"\n--- Tilanne {tunnit} tunnin jälkeen ---")
            kilpailu.tulosta_tilanne()

    print(f"\nKilpailu päättyi {tunnit} tunnin jälkeen!")
    print("\n=== Lopputilanne ===")
    kilpailu.tulosta_tilanne()

if __name__ == "__main__":
    main()