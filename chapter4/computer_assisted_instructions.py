import random


def assisted_instructions():
    number1 = random.randrange(1, 9)
    number2 = random.randrange(1, 9)
    answer = int(input(f"How much is {number1} times {number2}: "))
    if answer == number1 * number2:
        print("Very good!")

        while answer != number1 * number2:
            number1 = random.randrange(1, 9)
            number2 = random.randrange(1, 9)
            print("No. Please try again.")
            answer = int(input(f"How much is {number1} times {number2}: "))
            if answer == number1 * number2:
                print("Very good! ")


print(assisted_instructions())
