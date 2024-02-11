def character_frequency(string: str):
    diction = {}
    for k in string:
        key = k
        value = string.count(key)
        diction.update({key: value})
    return diction


word = 'semicolon.africa'
print(character_frequency(word))
