def split_a_list_in_half(string: list):
    str1 = str(''.join(string))
    result = list(str1.split())
    return result


sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
print(split_a_list_in_half(sample_input))
