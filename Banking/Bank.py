from Banking.Account import Account


class Bank:
    def __init__(self, bankName: str):
        self.__total_number_of_account = 0
        self.accounts: list = []

    def create_account(self, firstName: str, lastName: str, pin: str) -> Account:
        self.__total_number_of_account += 1
        account_number: str = self.__generate_account_number()
        account_name: str = self.__generate_account_name(firstName, lastName)
        account: Account = Account(account_name, account_number, pin)
        self.accounts.append(account)
        return account

    def __generate_account_number(self) -> str:
        return str(self.__total_number_of_account)

    def __generate_account_name(self, firstName: str, lastName: str) -> str:
        return firstName + " " + lastName

    def get_total_number_of_accounts(self) -> int:
        return len(self.accounts)

    def find_account(self, number: str):
        for account in self.accounts:
            if account.account_number() == number:
                return account
        return None

    def deposit(self, amount: int, number: str) -> None:
        account: Account = self.find_account(number)
        account.deposit(amount)

    def withdraw(self, number: str, pin: str, amount: int):
        account: Account = self.find_account(number)
        account.withdraw(amount, pin)

    def transfer(self, amount: int, sender: str, receiver: str, pin: str):
        account1: Account = self.find_account(sender)
        account2: Account = self.find_account(receiver)
        account1.withdraw(amount, pin)
        account2.deposit(amount)

    def remove(self, number: str, account=None):
        self.__total_number_of_account -= 1
        account: Account = self.find_account(number)
        self.accounts.remove(account)

    def check_balance(self, number: str, pin: str):
        account: Account = self.find_account(number)
        return account.check_balance(pin)
