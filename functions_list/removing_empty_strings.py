def remove_multiple_empty_strings(string: list):
    while "" in string:
        string.remove("")
    return string
