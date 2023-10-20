def biggest_odd_number(number: str):
    odd = []
    biggest = number[0]
    for i in number:
        if int(i) % 2 == 1:
            if i > biggest:
                biggest = i
    return biggest


def biggest_odd(numbers):
    largest = 0
    return int(max(filter(lambda n: int(n) % 2 == 1, numbers)))


def biggest_odd2(number3):
    return int(max([number for number in number3 if int(number) % 2 != 0]))


# number2 = '123457'
# print(biggest_odd2(number2))
