import random

def noppa(sivu):
    return random.randint(1, sivu)

koko = int(input("Kuinka isoa noppaa heitetään? "))
kerrat = int(input("Montako kertaa noppaa heitetään? "))

for i in range(kerrat):
    tulos = noppa(koko)
    print("Nopasta tuli", tulos)
