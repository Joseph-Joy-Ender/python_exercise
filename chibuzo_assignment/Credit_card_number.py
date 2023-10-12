def evenly_placed(creditCardNumber):
    total = 0
    index = len(creditCardNumber)
    while index > 0:
        if index % 2 != 0:
            result = (creditCardNumber[index - 1] * 2)
            if result > 9:
                total = total + add_numbers_bigger_than_nine(result)
            else:
                total = total + result
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
