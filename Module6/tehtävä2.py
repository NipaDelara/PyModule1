import random

def noppaa(tahkojen):
    return random.randint(1, tahkojen)


tahkojen = int(input("Anna nopan tahkojen määrä: "))

silmaluku = 0

while silmaluku != tahkojen:
    silmaluku = noppaa(tahkojen)
    print("Sait:", silmaluku)

print("Onneksi olkoon, sait suurimman luvun:", tahkojen)
