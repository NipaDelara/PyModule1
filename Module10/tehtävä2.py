class Hissi:
    def __init__(self, alin_kerros,  ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros #koska aloitus kerros

    def  kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros +=1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin_kerros or kohde_kerros < self.alin_kerros:
            print("Virheellinen kerros.")
            return

        print(f"Siirrytään kerrokseen {kohde_kerros}...")
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()
        print(f"Hissi on saapunut kerrokseen {self.nykyinen_kerros}.")
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_1km):
        self.hissit = []
        for i in range(hissien_1km):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)
        print(f"Talo luotu. Talossa on {hissien_1km} hissia.")

    def aja_hissia(self, hissin_numero, kohde_kerros):
        if hissin_numero < 0 or hissin_numero >= len(self.hissit):
            print("Virheellinen hissin numero.")
            return

        print(f"\nAjetaan hissiä numero {hissin_numero + 1}...")

        hissi = self.hissit[hissin_numero]
        hissi.siirry_kerrokseen(kohde_kerros)

def main():
    talo = Talo(1, 10, 3)

    talo.aja_hissia(0, 5)
    talo.aja_hissia(1, 8)
    talo.aja_hissia(0, 1)


if __name__ == "__main__":
    main()

