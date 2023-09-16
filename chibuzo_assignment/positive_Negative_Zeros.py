positiveCounter = 0
negativeCounter = 0
zeroCounter = 0

numbers = int(input("Enter numbers or enter -99 to terminate: "))

while numbers != -99:

    if numbers > 0:
        positiveCounter += 1
    elif numbers < 0:
        negativeCounter += 1
    elif numbers == 0:
        zeroCounter += 1
    numbers = int(input("Enter number or -99 to terminate: "))

print("Positive number is: ", positiveCounter)
print("Negative number is: ", negativeCounter)
print("zero number is: ", zeroCounter)
