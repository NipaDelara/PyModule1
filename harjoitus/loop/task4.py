import random
secret = random.randint(1,10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! The number was", secret)
        break
