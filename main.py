import random 

MAX_LINES = 3
MIN_BET = 10
MAX_BET = 50

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 10,
    "B": 5,
    "C": 3,
    "D": 2,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns  = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    #[[A, B, C],
    # [D. A. B],
    # [C. D. C]]
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row])

def calc_payout(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines-1):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += bet*values[symbol]
            winning_lines.append(line+1)
        
    return winnings, winning_lines
    # payout = 0
    # for line in range(lines-1):
    #     lines_bet = []
    #     for column in columns:
    #         lines_bet.append(column[line])
    #         symbol = lines_bet[0]
    #     if all(x == symbol for x in lines_bet):
    #         payout += (values[symbol]*bet)
    #     else:
    #         payout += 0
    # return payout  
    # code works^^  
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")

    return amount

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines*bet

        if total_bet > balance:
            print(f"You are betting ${total_bet} with an insufficient balance of ${balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    payout, winning_lines = calc_payout(slots,lines,bet,symbol_values)
    print(f"You won ${payout} !")
    print(f"Youn won on lines:", *winning_lines)
    return payout-total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to play (q to quit).")
        if spin == "q":
            break;
        balance += game(balance)
    print(f"You left with ${balance}")

main()