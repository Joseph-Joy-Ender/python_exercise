first_input = int(input("Enter first number: "))
second_input = int(input("Enter second number: "))
third_input = int(input("Enter third number: "))

if first_input > second_input and first_input > third_input:
    print(first_input, "is the highest number")

if second_input > first_input and second_input > third_input:
    print(second_input, "is the highest number")

if third_input > first_input and third_input > second_input:
    print(third_input, "is the highest number")
