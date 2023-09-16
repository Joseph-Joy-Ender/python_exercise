even = 0
odd = 0
for numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if numbers % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Number of even number is ", even)
print("Number of odd number is ", odd)
