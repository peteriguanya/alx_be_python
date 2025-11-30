class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner name cannot be empty.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"Deposited: ${amount:.1f}")
        return True  # <-- return True for unit tests

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            print("Insufficient funds.")
            return False  # <-- return False if insufficient
        self._balance -= amount
        print(f"Withdrew: ${amount:.1f}")
        return True  # <-- return True for unit tests

    def display_balance(self):
        print(f"Current Balance: ${self._balance:.2f}")

    def get_balance(self):
        return self._balance

