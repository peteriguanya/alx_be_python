from bank_account import BankAccount

def main():
    print("=== Simple Bank Account Program ===")

    # Create an account
    try:
        name = input("Enter account owner name: ")
        initial_balance = float(input("Enter initial balance: "))
        account = BankAccount(name, initial_balance)
    except ValueError as e:
        print(f"Error creating account: {e}")
        return

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        try:
            if choice == "1":
                amount = float(input("Deposit amount: "))
                new_balance = account.deposit(amount)
                print(f"Deposit successful. New balance: {new_balance}")

            elif choice == "2":
                amount = float(input("Withdraw amount: "))
                new_balance = account.withdraw(amount)
                print(f"Withdrawal successful. New balance: {new_balance}")

            elif choice == "3":
                print(f"Current balance: {account.get_balance()}")

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please enter 1–4.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
