vuosi = int(input("Anna vuosi : "))

if (vuosi % 4 == 0 & vuosi % 100 !=0) or (vuosi % 400 == 0):
    print("Vuosi on karkausvuosi.")

else:
    print("Vuosi ei ole karkausvuosia")