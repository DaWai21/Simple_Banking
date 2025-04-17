def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit(balance):
    amount = float(input("Enter the amount: "))
    if amount < 0:
        print("Invalid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount: "))
    if amount < 0:
        print("Invalid amount")
        return 0
    elif amount > balance:
        print("Insufficient amount")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True
    while is_running:

        print("1. Show balance")
        print("2. Deposit")
        print("3. withdraw")
        print("4. Exit")
        choice = int(input("Choose your action (1-4): "))
        if choice == 1:
            show_balance(balance)
        elif choice ==2:
            balance += deposit(balance)
            print(f"Your new balance is ${balance:.2f}")
        elif choice == 3:
            balance -= withdraw(balance)
            print(f"Your new balance is ${balance:.2f}")
        elif choice > 4:
            print("Invalid input")
        else:
            break
    print("Thank you. Have a nice day.")

if __name__ == '__main__':
    main()