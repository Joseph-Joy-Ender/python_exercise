from Banking import Account


class Bank:
    def __init__(self, bankName: str):
        self.__total_number_of_account = 0

    def create_account(self, firstName: str, lastName: str, pin: str) -> Account:
        self.__total_number_of_account += 1

