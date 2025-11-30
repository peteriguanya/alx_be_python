import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_initialization(self):
        account = BankAccount("Alice", 100)
        self.assertEqual(account.owner, "Alice")
        self.assertEqual(account._balance, 100)

    def test_invalid_owner(self):
        with self.assertRaises(ValueError):
            BankAccount("", 100)

    def test_negative_initial_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("Bob", -10)

    def test_deposit_valid(self):
        account = BankAccount("Charlie", 50)
        result = account.deposit(20)
        self.assertTrue(result)
        self.assertEqual(account._balance, 70)

    def test_deposit_invalid(self):
        account = BankAccount("Dana", 50)
        result = account.deposit(-10)
        self.assertFalse(result)
        self.assertEqual(account._balance, 50)

    def test_withdraw_valid(self):
        account = BankAccount("Eve", 100)
        result = account.withdraw(40)
        self.assertTrue(result)
        self.assertEqual(account._balance, 60)

    def test_withdraw_invalid_negative(self):
        account = BankAccount("Frank", 80)
        result = account.withdraw(-20)
        self.assertFalse(result)
        self.assertEqual(account._balance, 80)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("Grace", 30)
        result = account.withdraw(50)
        self.assertFalse(result)
        self.assertEqual(account._balance, 30)

    def test_display_balance_prints(self):
        import io
        import sys

        account = BankAccount("Henry", 123.45)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        account.display_balance()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Current Balance: $123.45")


if __name__ == "__main__":
    unittest.main()
