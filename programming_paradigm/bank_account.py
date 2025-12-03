class BankAccount:
    """A simple bank account class."""

    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds exist."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")



