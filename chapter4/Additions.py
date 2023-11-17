import random


def first_question():
    number1 = generate_random_number()
    number2 = generate_random_number()
    while True:
        answer = int(input(f'How much is {number1} plus {number2} '))
        if answer != number1 + number2:
            print(possible_response_to_incorrect_answer())
        if answer == number1 + number2:
            print(possible_response_to_correct_answer())
            number1 = generate_random_number()
            number2 = generate_random_number()


def generate_random_number():
    return random.randrange(1, 9)


def possible_response_to_correct_answer():
    message = ''
    rand = random.randrange(1, 5)
    match rand:
        case 1:
            message = "Very good!"
        case 2:
            message = "Excellent!"
        case 3:
            message: str = "Nice work!"
        case 4:
            message = "Keep up the good work!"
    return message


def possible_response_to_incorrect_answer():
    message = ''
    rand = random.randrange(1, 5)
    match rand:
        case 1:
            message = "No. Please try again."
        case 2:
            message = "Wrong. try once more."
        case 3:
            message: str = "Don't give up!"
        case 4:
            message = "No. keep trying.!"
    return message
