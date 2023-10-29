def two_list_to_dictionary(string1: list, string2: list):
    list3 = zip(string1, string2)
    result = dict(list3)
    return result

