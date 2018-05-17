from unittest import TestCase
from bankaccount import BankAccount


class BankAccountTest(TestCase):
    def test_balance(self):
        acc = BankAccount(100)
        self.assertEqual(110, acc.balance())
