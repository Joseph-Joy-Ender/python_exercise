def evenly_placed(creditCardNumber: list):
    total = 0
    index = len(creditCardNumber)
    while index > 0:
        if index % 2 != 0:
            result = (creditCardNumber[index - 1] * 2)
            total += result
            index -= 1
    return total


def add_numbers_bigger_than_nine(number):
    sums = 0
    while number > 0:
        remainder = number % 10
        sums += remainder
        number /= 10
    return sums


credit_number = [4388576018410707]
print(evenly_placed(credit_number))
