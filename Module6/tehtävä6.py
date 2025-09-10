import math

def yksikkohinta(halkaisija, hinta):
    sade = (halkaisija / 100) / 2
    ala = math.pi * sade * sade
    return hinta / ala


halkaisija1 = float(input("Anna 1. pizzan halkaisija (cm): "))
hinta1 = float(input("Anna 1. pizzan hinta (€): "))


halkaisija2 = float(input("Anna 2. pizzan halkaisija (cm): "))
hinta2 = float(input("Anna 2. pizzan hinta (€): "))


yh1 = yksikkohinta(halkaisija1, hinta1)
yh2 = yksikkohinta(halkaisija2, hinta2)

print("1. pizzan yksikköhinta:", round(yh1, 2), "€/m²")
print("2. pizzan yksikköhinta:", round(yh2, 2), "€/m²")

if yh1 < yh2:
    print("1. pizza on parempi ostos.")
elif yh2 < yh1:
    print("2. pizza on parempi ostos.")
else:
    print("Molemmat pizzat ovat yhtä hyviä.")
