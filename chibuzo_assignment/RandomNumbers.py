import random

number = int(input("Enter a number: "))
precious = random.randint(1, 10)

while number != precious:
    input("Enter a number: ")
precious = random.randint(1, 10)
# print(number)
if number == precious:
    print(number, "is the Correct answer")
else:
    input("Enter a number: ")
