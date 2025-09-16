gender = input("Enter gender(Female/Male): ")
value = float(input("Enter hemoglobin value (g/l): "))

if gender == "Female":
    if value < 117:
        print(f"Value is {value} g/l. Hemoglobin low.")
    elif  value >155:
        print(f"Value is {value} g/l. Hemoglobin High.")
    else:
        print(f"Value is {value} g/l. Hemoglobin normal.")


if gender == "Male":
    if value <134:
        print(f"Value is {value} g/l. Hemoglobin low.")
    elif  value > 167:
        print(f"Value is {value} g/l. Hemoglobin High.")
    else:
        print(f"Value is {value} g/l. Hemoglobin normal.")