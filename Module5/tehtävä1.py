import random
n = int(input("Montako arpakuutiota heitetään? "))

summa = 0

for i in range(n):
    silmäluku = random.randint(1,6)
    print("Noppa",i + 1, ":",silmäluku )

    summa = summa + silmäluku
print("Silmäluvut : ", summa)