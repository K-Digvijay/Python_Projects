import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_count = {"A": 5, "B": 4, "C": 3, "D": 2}


def get_check_winning(columns, lines, bet, values):
    winning = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
            else:
                winning += values[symbol] * bet
                winning_line.append(line + 1)
    return winning, winning_line


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # for _ in range(symbol_count):
        #     all_symbols.append(symbol)
        all_symbols.extend([symbol] * symbol_count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end=" ")
        print()


def deposit():
    while True:
        amount = input("What money to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater then 0")
        else:
            print("Please enter the valid number")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines")
        else:
            print("Please enter the valid number")

    return lines


def get_bet():
    while True:
        amount = input(f"what would like to bet on each line ({MIN_BET}-{MAX_BET}) ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter the valid number")

    return amount


def Spin(balance):
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Your current balance is = {balance}, your total bet is {total_bet}")
            print("Your have exceed your balance")
        else:
            break
    print(f"You are Betting {bet} on {lines}. total bet is = {total_bet}")
    print(f"Your remaining balance is: {balance-total_bet}")

    slot = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slot)

    win, win_line = get_check_winning(slot, lines, bet, symbol_count)
    print(f"You have won: {win} !!!!")
    print(f"you won on the line: {win_line} !!")

    return win - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current Balance is: {balance}")
        spin = input("Press 'Enter' to spin or 'q' to quit: ")
        if spin == "q":
            break
        else:
            balance += Spin(balance)
    print(f"You left with: {balance} Thank you for playing!!")
    print("DO VISIT AGAIN !!!")


main()
