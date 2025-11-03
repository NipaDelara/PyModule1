class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0.0

    def kiihdyta(self, nopeus):
        if nopeus < 0:
            self.nopeus = 0
        elif nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = nopeus

    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


# Pääohjelma
sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

# halutut nopeudet
sahkoauto.kiihdyta(120)
polttomoottoriauto.kiihdyta(100)

# Ajetaan 3 tuntia
sahkoauto.aja(3)
polttomoottoriauto.aja(3)

print(f"Sähköauto {sahkoauto.rekisteritunnus}: {sahkoauto.matkamittari} km")
print(f"Polttomoottoriauto {polttomoottoriauto.rekisteritunnus}: {polttomoottoriauto.matkamittari} km")
