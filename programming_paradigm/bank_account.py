class BankAccount:
    def __init__(self, owner, balance=0.0):
        if not owner.strip():
            raise ValueError("Owner name cannot be empty.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self._balance += amount
        print(f"Deposited: ${amount}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self._balance:
            print("Insufficient funds.")
            return False
        self._balance -= amount
        print(f"Withdrew: ${amount}")
        return True

    def display_balance(self):
        print(f"Current Balance: ${self._balance:.2f}")
