luku = int(input("Anna kokonaisluku: "))

onko_alkuluku = True

if luku < 2:
    onko_alkuluku = False
else:
    for i in range(2, luku):
        if luku % i == 0:
            onko_alkuluku =False
            break
if onko_alkuluku:
    print(luku, "on alkuluku.")
else:
    print(luku, "ei ole alkuluku.")
