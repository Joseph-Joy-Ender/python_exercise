first_number = 0
second_number = 1
series = 50
for i in range(2, series):
    if first_number >= 50:
        break
    print(first_number, ", ", end=" ")
    third_term = first_number + second_number
    first_number = second_number
    second_number = third_term

first_number = 0
second_number = 1
number = 2
while number <= 50:

    print(first_number, ", ", end=" ")
    third_term = first_number + second_number
    first_number = second_number
    second_number = third_term
    number += 1



