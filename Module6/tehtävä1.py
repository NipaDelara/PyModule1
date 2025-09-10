import random
def heita():
    return random.randint(1, 6)

luku = 0

while luku != 6:
    luku = heita()
    print("Sait:", luku)
