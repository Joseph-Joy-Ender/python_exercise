from chapter4 import Subtractions, Additions, Multiplications, Division


def subtraction_problems():
    Subtractions.first_question()


def addition_problems():
    Additions.first_question()


def multiplication_problems():
    Multiplications.first_question()


def division_problems():
    Division.first_question()


def menu():
    print("""
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      5. Random mixture
    """)
    options = int(input("select an option "))
    match options:
        case 1:
            addition_problems()
        case 2:
            subtraction_problems()
        case 3:
            multiplication_problems()
        case 4:
            division_problems()


print(menu())
