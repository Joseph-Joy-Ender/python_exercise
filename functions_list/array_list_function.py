def largest_element(number):
    largest = 0
    for i in number:
        if i > largest:
            largest = i

    return largest


def element_occurrence(first_number, second_number):
    if second_number in first_number:
        return True
    return False


def reverse_a_list(number1) -> int:
    reversed_list = number1
    reversed_list.reverse()
    return reversed_list


def running_total_of_a_list(number):
    total = 0
    i = 0
    while i < len(number):
        total += number[i]
        i += 1
        return total


def sum_of_list(lis):
    totals = 0
    for val in lis:
        totals = totals + val
    return totals


def odd_positions(odd_number):
    odd = odd_number[1::2]
    return odd


def even_positions(even_numbers):
    even = even_numbers[::2]
    return even


def is_palindrome(string: str):
    # string = string.lower()
    if len(string) <= 1:
        return True
    i = 0
    while i < len(string) / 2:
        if string[i] != string[len(string) - i - 1]:
            return False
        return True
