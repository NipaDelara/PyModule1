def gallo(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Anna bensiinin määrä , negatiivinen lopettaa: "))

    if gallonat < 0:
        print("Ohjelma päättyy.")
        break

    litrat = gallo(gallonat)
    print(gallonat, "gallonaa on", litrat, "litraa.")
