from Banking.InvalidAmount import InvalidAmount
from Banking.InvalidAmountException import InvalidAmountException
from Banking.InvalidPinException import InvalidPinException


class Account:
    def __init__(self, account_name: str, account_number: str, pin: str):
        self.__name = account_name
        self.__number = account_number
        self.__pin = pin
        self.__balance = 0

    def check_balance(self, pin: str):
        self.__validate(pin)
        return self.__balance

    def deposit(self, amount: int) -> None:
        self.__check_sufficient_funds(amount)
        self.__balance += amount

    def __validate(self, pin: str):
        if pin != self.__pin:
            raise InvalidPinException("Wrong pin")

    def __validate_amount(self, amount: int):
        if amount > self.__balance:
            raise InvalidAmountException("you have insufficient funds")

    def __check_sufficient_funds(self, amount: int):
        if amount < 0:
            raise InvalidAmount("Amount must be greater than zero")

    def withdraw(self, amount: int, pin: str):
        self.__validate(pin)
        self.__validate_amount(amount)
        self.__balance -= amount

    def account_number(self) -> str:
        return self.__number

    def __str__(self):
        return f"""
        Your Account details
        Account Name {self.__name}
        Account number {self.__number}
        Account balance {self.__balance}
        """
