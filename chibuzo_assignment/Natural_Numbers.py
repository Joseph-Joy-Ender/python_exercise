number = int(input("Enter ten natural numbers: "))
total = 0
last = number + 1

for i in range(1, last):
    total = total + i
print("The sum of ten natural numbers = ", total)
