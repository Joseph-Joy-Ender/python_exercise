import random


def guess_number():
    condition = True
    while condition:
        guesses = int(input("Guess my number between 1 and 9 with the fewest guesses: "))
        guess = random.randrange(1, 2)
        if guesses > guess:
            print("Too high, try again.")
        if guesses < guess:
            print("Too low, try again.")
        if guesses != guess:
            print("Guess my number between 1 and 9: ")
            guesses = input()
        if guesses == guess:
            print("Congratulations. You guessed the number!")
            print("Do you want to play again?")
            answer = input()
            if answer == "No":
                condition = False


print(guess_number())
