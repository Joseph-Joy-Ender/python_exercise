sample_list = [1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]


def unique_list():
    sets = set()
    for i in sample_list:
        if i % 2 == 0:
            sets.add(i)
    return sets


print(unique_list())
