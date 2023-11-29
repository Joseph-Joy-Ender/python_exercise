import random


def first_question():
    counter = 1
    score = 0
    percentage = 0
    number1 = generate_random_number()
    number2 = generate_random_number()
    while counter <= 10:
        answer = get_answer(number1, number2)
        if answer == number1 * number2:
            score = score + 1
            print(possible_response_to_correct_answer())
            number1 = generate_random_number()
            number2 = generate_random_number()
        counter = counter + 1
        percentage = (score / counter) * 100
    percentage_method(percentage)


def get_answer(number1, number2):
    answer = int(input(f'How much is {number1} times {number2} '))
    if answer != number1 * number2:
        print(possible_response_to_incorrect_answer())
    return answer


def percentage_method(percentage):
    if percentage < 75:
        print("Please ask your teacher for extra help")
    else:
        print("Congratulations, you are ready to go to the next level")


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


first_question()
