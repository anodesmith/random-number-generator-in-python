import random

number = random.randint(1,100)

while True:
    guess = int(input("Guess the number between 1 and 100"))

    if guess == number:
        print("Congratulations, you guessed correctly")

    elif guess < number:
        print("too low, guess again")

    else:
        print("too high, guess again")