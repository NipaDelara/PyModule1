correct_username = "python"
correct_password = "rules"
tring = 0

while tring < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Username or password wrong. Try again!")
        tring += 1
if tring == 5:
    print("Access denied!")
