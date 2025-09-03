luku =[]

while True:
    syote= input("Anna luku (tyhjä lopettaa): ")
    if syote == "" :
        break
    luku.append(float(syote))

if luku:
    print("Pienin: ", min(luku))
    print("Suurin: ", max(luku))

else:
    print("Et antanut lukua.")
