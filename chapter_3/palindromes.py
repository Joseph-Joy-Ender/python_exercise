number = int(input("Enter a five digit number: "))
first = number // 10000 % 10
second = number // 1000 % 10
third = number // 100 % 10
fourth = number // 10 % 10
fifth = number % 10

if first == fifth:
    print("This is a palindrome")
else:
    print('Number is not a palindrome')
