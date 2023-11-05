def difference(strings: list):
    largest = strings[0]
    smallest = strings[0]
    for i in strings:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    differences = largest - smallest
    return differences

