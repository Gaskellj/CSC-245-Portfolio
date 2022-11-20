import random


def play():
    secret_number = random.randint(1,100)
    distance = 100

    print("I have chosen a secret number between 1 and 100. What number is it?")

    guess = int(input("Please make a guess "))

    while guess != secret_number:
        if guess > secret_number:
            guess = int(input("The secret number is lower than that. Try again."))
        else:
            guess = int(input("The secret number is higher than that. Try again."))
        if abs(secret_number - guess) < distance:
            print("You're getting warmer.")
        elif abs(secret_number - guess) > distance:
            print("You're getting colder.")
        distance = abs(secret_number - guess)

    print("Yay! You guessed it. My secret number was ", secret_number)

play()
