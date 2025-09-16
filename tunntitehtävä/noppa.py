import random
heitot = 0
noppa1 = random.randint(1, 6)
noppa2 = random.randint(1, 6)

while (noppa1!=6 or noppa2!=6):

    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    heitot = heitot + 1

print(f"Tarvittiin {heitot:d} heittoa.")