def laske_sum(numerot):
    summa = 0
    for luku in numerot:
        summa += luku
    return summa

numerolista = [3, 7, 2, 8, 5]
tulos = laske_sum(numerolista)

print("Listan luvut:", numerolista)
print("Listan lukujen summa on:", tulos)
