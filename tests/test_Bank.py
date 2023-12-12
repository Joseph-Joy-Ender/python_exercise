from unittest import TestCase

from Banking.Account import Account
from Banking.Bank import Bank


class TestBank(TestCase):
    def test_create_account(self):
        bank: Bank = Bank("BankName")
        account: Account = bank.create_account("FirstName", "LastName", "1234")
        self.assertEqual("1", account.account_number())
        self.assertEqual(1, bank.get_total_number_of_accounts())

    def test_that_i_can_find_account_with_account_number(self):
        bank: Bank = Bank("BankName")
        first_account: Account = bank.create_account("First", "last", "1234")
        second_account: Account = bank.create_account("second", "Sunday", "1235")
        self.assertEqual(first_account, bank.find_account("1"))
        self.assertEqual(second_account, bank.find_account("2"))

    def test_that_i_can_deposit2k_to_account_with_account_number(self):
        bank: Bank = Bank("BankName")
        account: Account = bank.create_account("Joy", "joseph", "1234")
        bank.deposit(2_000, "1")
        self.assertEqual(account.check_balance("1234"), 2_000)

    def test_thatICanDeposit2kAndWithdraw1k(self):
        bank: Bank = Bank("BankName")
        account: Account = bank.create_account("Joy", "joseph", "1234")
        bank.deposit(2_000, "1")
        bank.withdraw("1", "1234", 1_000)
        self.assertEqual(account.check_balance("1234"), 1_000)

    def test_ThatICanDeposit5kAndTransfer3kToAnotherAccount(self):
        bank: Bank = Bank("BankName")
        first_account: Account = bank.create_account("FirstName", "LastName", "1234")
        second_account: Account = bank.create_account("First name", "last name", "1234")

        self.assertEqual(first_account, bank.find_account("1"))
        self.assertEqual(second_account, bank.find_account("2"))

        bank.deposit(5_000, "1")
        bank.transfer(3_000, "1", "2", "1234")

        self.assertEqual(2_000, first_account.check_balance("1234"))
        self.assertEqual(3_000, second_account.check_balance("1234"))

    def test_thatAccountCanBeRemoved(self):
        bank: Bank = Bank("BankName")
        first_account: Account = bank.create_account("FirstName", "LastName", "1234")
        second_account: Account = bank.create_account("First name", "last name", "1234")
        self.assertEqual(2, bank.get_total_number_of_accounts())
        bank.remove("1")
        self.assertEqual(1, bank.get_total_number_of_accounts())
