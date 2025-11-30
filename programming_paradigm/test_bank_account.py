import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_initialization(self):
        account = BankAccount("Alice", 100)
        self.assertEqual(account.owner, "Alice")
        self.assertEqual(account.balance, 100)

    def test_invalid_owner(self):
        with self.assertRaises(ValueError):
            BankAccount("", 100)

    def test_negative_initial_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("Bob", -10)

    def test_deposit_valid(self):
        account = BankAccount("Charlie", 50)
        account.deposit(20)
        self.assertEqual(account.get_balance(), 70)

    def test_deposit_invalid(self):
        account = BankAccount("Dana", 50)
        with self.assertRaises(ValueError):
            account.deposit(-5)

    def test_withdraw_valid(self):
        account = BankAccount("Eve", 100)
        account.withdraw(40)
        self.assertEqual(account.get_balance(), 60)

    def test_withdraw_invalid_negative(self):
        account = BankAccount("Frank", 80)
        with self.assertRaises(ValueError):
            account.withdraw(-10)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("Grace", 30)
        with self.assertRaises(ValueError):
            account.withdraw(100)

if __name__ == "__main__":
    unittest.main()


