from Banking.Account import Account
from Banking.Bank import Bank
from Banking.InvalidAmount import InvalidAmount
from Banking.InvalidPinException import InvalidPinException


def create_account():
    first_name: str = input("Enter first name: ")
    last_name: str = input("Enter last name: ")
    pin: str = input("Enter your pin: ")

    account: Account = bank.create_account(first_name, last_name, pin)
    print("Account successfully created")
    print(account.__str__())
    main_menu()


def deposit():
    amount: int = int(input("Enter amount to deposit: "))
    number: str = input("Enter account number: ")
    bank.deposit(amount, number)

    print("Your deposit was successful")
    main_menu()


def withdraw():
    number: str = input("Enter account number: ")
    amount: int = int(input("Enter amount to withdraw: "))
    pin: str = input("Enter your pin: ")

    bank.withdraw(number, pin, amount)
    main_menu()


def transfer():
    try:
        sender: str = input("Enter the sender account number: ")
        receiver: str = input("Enter the receiver account number: ")
        amount: int = int(input("Enter amount to transfer: "))
        pin: str = input("Enter pin: ")
        bank.transfer(amount, sender, receiver, pin)
        main_menu()
    except InvalidPinException:
        print("Invalid pin")
    except InvalidAmount:
        print("Invalid amount")


def check_balance():
    try:
        number: str = input("Enter your account number: ")
        pin: str = input("Enter your pin: ")
        print("Balance is ", bank.check_balance(number, pin))
        main_menu()
    except InvalidPinException:
        print("Wrong pin")
        check_balance()


def remove_account():
    number: str = input("Enter your account number: ")
    bank.remove(number)
    main_menu()


def exit_program():
    exit(2)


bank: Bank = Bank("Globus")


def main_menu():
    menu_map()
    inputs = int(input())
    match inputs:
        case 1:
            create_account()
        case 2:
            deposit()
        case 3:
            withdraw()
        case 4:
            transfer()
        case 5:
            check_balance()
        case 6:
            remove_account()
        case 7:
            exit_program()


def menu_map():
    menu: str = """
      ===================================
            Welcome to UBA
      ===================================
      1 -> create account
      2 -> deposit
      3 -> withdraw
      4 -> transfer
      5 -> check balance
      6 -> remove account
      7 -> exit program
    """
    print(menu)


main_menu()
