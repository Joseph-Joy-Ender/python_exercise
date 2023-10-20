def list_of_given_number(first, second):
    numbers = []
    for number in range(first, second):
        numbers.append(number)
    return numbers


def odd_numbers_in_a_list(numbs):
    odd_numbers = []
    for number in numbs:
        if number % 2 == 1:
            odd_numbers.append(number)
    return odd_numbers


def double_item_in_list(lists):
    for number in range(len(lists)):
        lists[number] **= 2
    return lists


def change_of_element(lists):
    for index, numbs in enumerate(lists):
        if 4 <= index <= 7:
            lists[index] = 0
    return lists


def empty_list(lists: list):
    lists.clear()
    return lists


def concatenate_list(first, second):
    lists = []
    for index in range(len(first)):
        strs = " "
        strs = first[index] + second[index]
        lists.append(strs)
    return lists
