def my_sort_function(list1: list):
    for i in range(0, len(list1)):
        for number in range(i + 1, len(list1)):
            if list1[i] >= list1[number]:
                list1[i], list1[number] = list1[number], list1[i]
        return list1


numbers = [10, 2, 9, 3, 6, 8, 18]
print(my_sort_function(numbers))

number2 = []
for i in range(1, 11):
    number2.append(i)
print(number2)

result = [i for i in range(1, 11) if i % 2 == 0]
print(result)

p