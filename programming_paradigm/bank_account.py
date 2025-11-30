class BankAccount:
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self._balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self._balance += amount
        print(f"Deposited: ${amount:.1f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self._balance:
            print("Insufficient funds.")
            return False
        self._balance -= amount
        print(f"Withdrew: ${amount:.1f}")
        return True

    def display_balance(self):
        print(f"Current Balance: ${self._balance:.2f}")

