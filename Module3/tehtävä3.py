sukupuoli = input("Anna biologisen sukupuolen (nainen/mies) : ")
arvo = int(input("Anna hemoglobiiniarvon (g/l): "))

if sukupuoli == "nainen":
    if arvo < 117 :
        print("Hemoglobiini alhainen")
    elif arvo > 175 :
        print("Hemoglobiini korkea")
    else:
        print("Hemoglobiini normaali")
#Mies Hemoglobiini
if sukupuoli == "mies":
    if arvo < 134 :
        print("Hemoglobiini alhainen")
    elif arvo > 195 :
        print("Hemoglobiini korkea")
    else:
        print("Hemoglobiini normaali")