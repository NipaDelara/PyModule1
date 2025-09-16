while True:
        vuosi= float(input("anna vuosi: "))

        if vuosi< 1896:
            print("Olympialaisia ei järestetty ennen vuosi  ")

        else:
            if vuosi % 4 == 0:
                print(f"vuosi on järstelmävuosi")

            else:
                print(f"Ei ollut järjestelmävuosi")



