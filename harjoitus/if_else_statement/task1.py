length = float(input("Enter the length of a Zander in (centimeter): "))
limit = 42

if length<limit:
    differ = limit - length

    print(f"The fish size is {differ:.1f}. Zander fish does not fulfill the size limit. Release the fish back into the lake. ")

else:
    print("This Zander fish is meet to the size limit. Yon can take.")


