def pattern1(numberOfShape: int):
    for i in range(0, numberOfShape):
        print()
        for j in range(0, i + 1):
            print("* ", end=' ')
        #  return numberOfShape


def pattern2(numberOfShape: int):
    for i in range(numberOfShape, 0, -1):
        for j in range(0, i):
            print("* ", end=' ')
        print()


def pattern3(number: int):
    for i in range(0, number):
        print("* ", end=' ')


pattern1(5)
print()
pattern3(6)
print()
pattern2(5)
