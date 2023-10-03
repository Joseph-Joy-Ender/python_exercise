number = int(input('enter ten integers: '))

first_largest_number = number
second_largest_number = number

for i in range(1, 10):
    second_number = int(input('Enter ten integers: '))
    if second_number > first_largest_number:
        second_largest_number = first_largest_number
        first_largest_number = second_number

print(first_largest_number)
print(second_largest_number)