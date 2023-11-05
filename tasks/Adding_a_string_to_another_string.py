def add_to_string(string: str):
    word = 'ing'
    second = 'ly'
    if len(string) >= 3:
        if string.endswith(word):
            string = string.__add__(second)
        else:
            string = string.__add__(word)
        return string
    elif len(string) < 3:
        return string
