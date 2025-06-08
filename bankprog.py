def Show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")


def Deposit(balance):
    amount = float(input("Enter an amount to Deposited: "))
    if amount < 0:
        print("Please enter valid amount")
        return 0
    else:
        print(f"Your previous amount is: {balance:.2f}")
        return amount


def Withdraw(amount):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient Funds")
        return amount
    elif amount < 0:
        print("Amount must be greater than Zero")
    else:
        print(f"your balance is: {balance:.2f}")
        return amount


balance = 0
is_running = True

while is_running:
    print("Banking program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choise = input("Enter your choise(1-4): ")

    if choise == '1':
        Show_balance(balance)
    elif choise == '2':
        balance += Deposit(balance)
    elif choise == '3':
        balance -= Withdraw(balance)
    elif choise == '4':
        is_running = False
        print(f"thank you for Banking with us!! Your Available Balance is {balance:.2f}")
    else:
        print("Please select valid choise")
    
    if is_running == '4':
            again = input("Do you want to continue? (y/n): ").strip().lower()
            if again != 'y':
                is_running = False
                print(f"Goodbye! Your final balance is ${balance:.2f}")

