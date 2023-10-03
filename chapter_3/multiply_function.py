number = []


def multiply(*number):
    product = 1
    for i in number:
        product *= i
        return product


print(multiply(12))
