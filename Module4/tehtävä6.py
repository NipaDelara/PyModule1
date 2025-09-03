import random

n =int(input("Montako pistetta? "))
N = 0
for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x * x + y * y <= 1:
        N = N + 1
pi = 4 * N / n
print("Piin likiarvo: ", pi)
