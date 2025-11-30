import sys
from bank_account import BankAccount

def main():
    account = BankAccount("TestUser", 250.0)

    if len(sys.argv) < 2:
        print("Usage: python main-1.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)  # Prints only once
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
