import random
numero = random.randint(1,10)
while True:
    valinta = int(input("Valita numero (1-10): "))

    if valinta > numero:
        print("Liian suuri arvaus")
    elif valinta<numero:
        print("Liian pieni arvaus")
    else:
        print("Oikein!")
        break