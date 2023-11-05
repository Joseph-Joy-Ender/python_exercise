def replacing_first_char(word: str, first_char: str, sign: str):
    word = word.replace(first_char, sign)
    return first_char + word[1:]


signs = '$'
words = 'restaurant'
first_character = 'r'
print(replacing_first_char(words, first_character, signs))
