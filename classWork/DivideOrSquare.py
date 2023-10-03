import math


def divide_or_square(number):
    square = number ** 0.50
    if number % 5 == 0:
        return square
    else:
        return number % 5


result = divide_or_square(5)
print(f'{result:.2f}')
