def sum_list(numbers):
    total = 0
    for i in numbers:
        for j in i:
            total += j
    return total


number = [[2, 4, 5, 6], [2, 3, 5, 6]]
print(sum_list(number))

totals = 0
for qudus in number:
    totals += sum(qudus)
print(totals)

a, b = number
result = sum(a) + sum(b)
print(result)
