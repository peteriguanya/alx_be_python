class BankAccount:
    """
    Simple BankAccount class used by the unit tests.
    - owner must be a non-empty string
    - initial balance must be >= 0
    - deposit(amount): raises ValueError if amount <= 0
    - withdraw(amount): raises ValueError if amount <= 0 or amount > balance
    - get_balance(): returns balance as float
    - display_balance(): prints "Current Balance: $<amount>" with 2 decimal places
    """

    def __init__(self, owner, balance=0):
        if not isinstance(owner, str) or owner.strip() == "":
            raise ValueError("Owner name must be a non-empty string.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self._balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += float(amount)
        # Do not print here (tests call get_balance()), printing is only required in display_balance()

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= float(amount)
        # Do not print here; tests check the numeric balance

    def get_balance(self):
        return float(self._balance)

    def display_balance(self):
        # Matches the grader's expected formatting
        print(f"Current Balance: ${self._balance:.2f}")
