def list_to_dictionary(strings: list):
    dicts = {}
    for i in strings:
        letter = i[0].lower()
        if letter in dicts:
            letter = i[0].upper()
        dicts.update({letter: i})
    return dicts

