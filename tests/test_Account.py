from unittest import TestCase

from Banking.Account import Account
from Banking.InvalidAmount import InvalidAmount
from Banking.InvalidAmountException import InvalidAmountException
from Banking.InvalidPinException import InvalidPinException


class TestAccount(TestCase):
    def test_deposit(self):
        account: Account = Account("Stanbic", "9018296", "1234")
        account.deposit(2_000)
        self.assertEqual(2_000, account.check_balance("1234"))

    def test_thatICannotDepositNegative(self):
        account: Account = Account("Stanbic", "9018296", "1234")
        with self.assertRaises(InvalidAmount):
            account.deposit(-2_000)

    def test_thatPinMustBeCorrect(self):
        account: Account = Account("Stanbic", "9018296", "1234")
        with self.assertRaises(InvalidPinException):
            account.check_balance("123456")

    def test_thatICanDeposit3_000_andWithdraw1_000(self):
        account: Account = Account("Stanbic", "9018296", "1234")
        account.deposit(3_000)
        account.withdraw(1_000, "1234")
        self.assertEqual(2_000, account.check_balance("1234"))
