# Python Banking Program

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("Invalid Amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter the amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running == True:
    print("Banking Program!")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        show_balance()
    elif choice == "2":
        balance += deposit()
        print(f"Your balance is now {balance}")
    elif choice == "3":
        balance -= withdraw()
        print(f"Your balance is now {balance}")
    elif choice == "4":
        is_running = False
    else:
        print("That is not a valid choice")

print("Thank you! Have a nice day.")

