class BankAccount:
    """
    BankAccount class with owner and balance
    """

    def __init__(self, owner, initial_balance=0):
        if not owner:
            raise ValueError("Owner name cannot be empty.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self._balance = float(initial_balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += float(amount)
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= float(amount)
        print(f"Withdrew: ${amount}")

    def display_balance(self):
        print(f"Current Balance: ${self._balance:.2f}")

    def get_balance(self):
        """Return the current balance (used by unit tests)."""
        return self._balance

    @property
    def balance(self):
        """Allow direct access to balance (some tests expect this)."""
        return self._balance
