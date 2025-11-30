from bank_account import BankAccount

def main():
    # Create account with owner and initial balance
    account = BankAccount("Peter", 250)

    # Deposit example
    deposit_amount = 67
    account.deposit(deposit_amount)  # prints Deposited: $67.0

    # Withdraw example
    withdraw_amount = 50
    if not account.withdraw(withdraw_amount):
        print("Insufficient funds.")  # only prints if withdraw fails

    # Attempt to withdraw more than balance
    withdraw_amount = 300
    if not account.withdraw(withdraw_amount):
        print("Insufficient funds.")

    # Display final balance
    account.display_balance()  # prints Current Balance: $250.00

if __name__ == "__main__":
    main()
