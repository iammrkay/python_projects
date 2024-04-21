import random

MAX_lines = 3
MAX_bet = 100
MIN_bet = 1

ROWS = 3
COLS = 3
symbox_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_slot_mahcine(ROWS,COLS,symbols):
    all_symbox = []
    for symbol, symbox_count in symbols.items():
        for _ in range(symbox_count):
            all_symbox.append(symbol)
    
    columns = []
    for _ in range(COLS):
        colimn = []
        current_symbos = all_symbox[:]
        for _ in range(ROWS):
            value = random.choice(current_symbos)
            current_symbos.remove(value)
        columns.append(value)
    for i in columns:
        print(columns)
    return columns
    

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end = " | ")
            else:
                print(column[row],end="")
        print()
    



def deposit():
    while True:
        amt = input("Enter the amount :")
        if amt.isdigit():
            amt = int(amt)
            if amt > 0:
                break
            else:
                print("Amount cannot be 0 ")
        else:
            print("Please enter a valid amount")
    return(amt)

def get_number_of_lines():
    while True:
        line  = input("Enter number of lines 1 -"+str(MAX_lines) + "? ")
        if line.isdigit():
            line = int(line)
            if (1 <= line <= MAX_lines):
                break
            else:
                print("enter a valid number of lines  ")
        else:
            print("Please enter a numbert")
    return(line)    

def get_bet():
    while True:
        amt = input("Enter the amount to bet: ")
        if amt.isdigit():
            amt = int(amt)
            if MIN_bet <= amt <= MAX_bet:
                break
            else:
                print(f"Amount bust be between {MIN_bet} - {MAX_bet}")
        else:
            print("Please enter a valid amount")
    return(amt)  


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"you do not have suffecient amount to bet, \n Your balance is {balance}")
        else:
            break
    print(f"you are betting {bet} on {lines} lines \n Total bet is {total_bet}")

    slots = get_slot_mahcine(ROWS,COLS,symbox_count)
    print_slot_machine(slots)


main()