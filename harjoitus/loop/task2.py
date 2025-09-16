while True:
    inches = float(input("Enter number (negative to quit): "))
    if inches<= 0:
        print("program end")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters:.2f} cm ")

