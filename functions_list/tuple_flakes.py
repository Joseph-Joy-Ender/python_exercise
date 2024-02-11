def tuples1(tuple1):
    new_tuple = ()
    for j in range(len(tuple1) - 1, -1, -1):
        new_tuple += (tuple1[j],)
    return new_tuple


def swapped_tuple(tuple9):
    first_variable = tuple9[0]
    second_variable = tuple9[-1]
    third_variable = second_variable
    second_variable = first_variable
    return third_variable, second_variable


tuple2 = ('orange', [10, 20, 30], (5, 15, 25))
new_tup = ()
first = (tuple2[1][1])
second = (tuple2[2][2])
print(first, second)


def more_than_one_tuple(tuple5):
    result = 1
    temp = []
    for i in range(len(tuple5)):
        for j in range(i + 1, len(tuple5)):
            if tuple5[i] == tuple5[j] and tuple5[i] not in temp:
                result = temp.append(tuple5[i])
        return result


my_playlist = []
names = ["joy", "Joseph", "Ope"]
name2 = list('Israel')
name3 = names + name2
print(name3)
list_to_tuple = tuple(names)
print(list_to_tuple)
tuple_to_list = list(list_to_tuple)
print(tuple_to_list)
# tuples5 = (20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5)
# print(more_than_one_tuple(tuples5))
print1 = 1, 2, 3
print2 = 'a', 'b', 'c'
print3 = print2 + print1
print(print3)
