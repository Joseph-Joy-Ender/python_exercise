
def patter1(numberOfShape: int):
    for i in range(1, numberOfShape):
        for i1 in range(i, numberOfShape + 1):
            print(" ", end="")
        for i2 in range(0, i):
            print("* ", end="")
        print()


def patter2(numberOfShapes):
    for i in range(numberOfShapes, 0, -1):
        for i1 in range(i, numberOfShapes + 1):
            print(" ", end="")
        for j in range(i, 0, -1):
            print("* ", end="")
        print()


number = int(input("Enter number of rows: "))
patter1(number)
patter2(number)
