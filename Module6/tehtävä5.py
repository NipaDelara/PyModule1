def poista_pari(numerot):
    uusi_lista = []
    for luku in numerot:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista


numerolista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu = poista_pari(numerolista)

print("Alkuperäinen lista:", numerolista)
print("Parilliset luvut:", karsittu)
