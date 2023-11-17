import random


def first_question():
    number1 = generate_random_number()
    number2 = generate_random_number()
    while True:
        answer = int(input(f'How much is {number1} times {number2}'))
        if answer != number1 * number2:
            print("No. please try again")
        if answer == number1 * number2:
            print("Very good")
            number1 = generate_random_number()
            number2 = generate_random_number()


def generate_random_number():
    return random.randrange(1, 9)


print(first_question())
