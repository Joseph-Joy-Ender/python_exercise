from chapter4 import Reducing_Student_Fatigue, Level2, Level3


def level1():
    Reducing_Student_Fatigue.first_question()


def level2():
    Level2.first_question()


def level3():
    Level3.first_question()


def menu():
    print("""
      Difficult level 1
      Difficult level 2
      Difficult level 3
    """)
    options = int(input("Select an option"))
    match options:
        case 1: level1()
        case 2: level2()
        case 3: level3()


print(menu())
