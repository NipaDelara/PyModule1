leiviskat = float(input("Leiviskät: "))
naulat = float(input("Naulat: "))
luodit = float(input("Luodit: "))

#Laske
grammat = (leiviskat*20*32 + naulat*32 + luodit) * 13.3

kg = int(grammat // 1000)
g = grammat % 1000

print("Massa nykymittojen mukaan: ")
print(kg, "kg ja", round(g, 2), "g")
