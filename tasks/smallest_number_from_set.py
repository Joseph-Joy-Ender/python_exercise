def smallest_from_set(input1: set, input2: set):
    answer = input1.intersection(input2)
    smallest = min(answer)
    return smallest


# first = {5, 4, 11, 13, 9}
# second = {9, 11, 15, 1, 14}
# print(smallest_from_set(first, second))
#
# inputs1 = {2, 3, 5, 6, 7, 8}
# inputs2 = {1, 3, 7, 10, 11, 8}
# print(smallest_from_set(inputs1, inputs2))
