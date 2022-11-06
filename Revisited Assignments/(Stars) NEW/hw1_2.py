import random

def play2(secret_number,distance):
    guess = int(input("Please make a guess "))
    if guess == secret_number:
        you_win(secret_number)
    elif guess > secret_number:
        print("The secret number is lower than that. Try again.")
    else:
        print("The secret number is higher than that. Try again.")
    
    new_distance = abs(secret_number - guess)
    if new_distance > distance:
        print("You're getting colder.")
    else:
        print("You're getting warmer.")
        
    play2(secret_number, new_distance)

def you_win(secret_number):
    print("Yay! You guessed it. My secret number was ", secret_number)
    quit()
    
    
play2(random.randint(1,100),100)
