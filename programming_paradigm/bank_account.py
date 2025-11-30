class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited ${amount}. New balance: ${self._balance}.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}.")

    def display_balance(self):
        print(f"Current Balance: ${self._balance:.2f}")


