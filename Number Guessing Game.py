import random


print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
print("I have selected a number between 1 and 100.")
print("Can you guess it?")
number_of_guess = 0


while True:
    guess = int(input("Guess the number: "))
    number_of_guess += 1
    if number < guess:
        print("Too high!")
    elif number > guess:
        print("Too low!")
    elif number == guess:
        print(f"Congratulations! You guessed the correct number {guess} in {number_of_guess}  attempts!")
