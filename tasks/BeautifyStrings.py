def add_full_stop(word: str):
    index = len(word) - 1
    last = word[-1]
    if last.endswith('.'):
        return word
    else:
        return word.__add__('.')


def capitalize_letter(string: str):
    result = string[0]
    replaced = (string[0] + "").upper() 
    print(replaced)
    string = string.replace(result, replaced)
    return string


def add_full_stop_and_capitalize(words: str):
    return add_full_stop(capitalize_letter(words))


sentence = "ender"
print(add_full_stop_and_capitalize(sentence))
