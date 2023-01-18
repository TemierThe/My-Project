import random

# глобальные константы (неизменяемые)
MAX_LINES = 3    # макс. линий автомата
MAX_BET   = 100  # макс. ставка
MIN_BET   = 10   # мин. ставка

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):    # анонимная переменная (одноразовая)
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):  # анонимная переменная (одноразовая)
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):   # анонимная переменная (одноразовая)
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print (column[row], end=" | ")
            else:
                print (column[row], end="")
        
        print()


def deposit():
    while True:
        amount = input ("Сколько ты хотел внести депозита ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print ("Число должно быть больше нуля.")
        else:
            print ("Пожалуйста введите число.")
    return amount


def get_number_of_lines():
    while True:
        lines = input ("Введите количество линий для старта, от 1 до " + str(MAX_LINES) + " ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print ("Введите допустимое количество строк.")
        else:
            print ("Введите число.")
    return lines

def get_bet():
    while True:
        amount = input ("Сколько бы ты хотел поставить на каждой линии? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:         # f-строка, авто замена типа переменной на str + удобство чтения
                print (f"Число должно быть между ${MIN_BET} - ${MAX_BET}")
        else:
            print ("Пожалуйста введите число.")
    return amount

def spin(balance):
    lines     = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print (f"Денег не хватит, Ваш текущий баланс - ${balance}")
        else:
            break

    print (f"Ты ставишь ${bet} на {lines} линии. Общая ставка равна: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Ты выиграл ${winnings}.")
    print (f"Ты выиграл на линии", *winnings_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Текущий баланс равен ${balance}")
        answer = input("Нажмите Enter для начала игры (Q - выход)").lower()
        if answer == "q":
            break
        balance += spin(balance)
    
    print (f"Ты ушел с этим ${balance}")


main()