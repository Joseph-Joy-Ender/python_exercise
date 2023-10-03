
number = int(input('Enter five digit integer: '))

sums = 0
while number > 0:
    number1 = number % 10
    number = number // 10

    sum += number1

print("\n sum of the digits of a given number is = %d" % sum)
