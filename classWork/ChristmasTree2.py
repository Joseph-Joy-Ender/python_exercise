def patter1(numberOfShape):
    for i in range(1, numberOfShape):
        for i1 in range(i, numberOfShape + 1):
            print(" ", end="")
        for i2 in range(0, i):
            print("* ", end="")
        print()


def print_out():
    print("   MERRY CHRISTMAS")


def pattern2():
    print("         **")
    print("         **")
    print("         **")


patter1(11)
print_out()
pattern2()