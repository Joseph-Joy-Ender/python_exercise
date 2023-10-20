def equal_strings(string1: str, string2: str):
    if len(string1) == len(string2):
        return True
    else:
        return False


name1 = 'loves'
name2 = 'evol'
print(equal_strings(name1, name2))
