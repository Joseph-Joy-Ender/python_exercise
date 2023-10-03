evenCount = 0
average = 0
counter = 0

for counts in range(0, 51, 2):
    print(counts, end=" ")
    evenCount += counts
    counter = counter + 1
    average = evenCount / counter
    print()
print(f'The sum of the number is {counter}')
print(f'The total number of even number is {evenCount}')
print(f'The average of the e  ven numbers is {average}')
