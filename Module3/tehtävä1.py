alamitta = 37

pituus = float(input("anna kuhan pituus cm: "))

if pituus < alamitta :
    puuttuu = pituus - alamitta
    print(f"kala on alamittainen. Takaisin järveen! se on {puuttuu} cm lylyt")

else:
    print("Kala on sallitun mittainen.Voit otta.")