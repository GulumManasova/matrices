import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("  A B C D E F G")
    print(" +-+-+-+-+-+-+-+")
    for i, row in enumerate(board):
        print(f"{i + 1}|{'|'.join(row)}|")
        print(" +-+-+-+-+-+-+-+")

def is_valid_location(board, ship, direction, row, col):
    length = len(ship)
    if direction == 'v':
        return row + length <= len(board) and all(board[i][col] == ' ' for i in range(row, row + length))
    elif direction == 'h':
        return col + length <= len(board[0]) and all(board[row][i] == ' ' for i in range(col, col + length))
    return False

def place_ship(board, ship, direction):
    while True:
        try:
            if direction == 'v':
                row = int(input("Введите номер строки (1-7): ")) - 1
                col = int(input("Введите номер столбца (1-7): ")) - 1
            elif direction == 'h':
                row = int(input("Введите номер строки (1-7): ")) - 1
                col = ord(input("Введите букву столбца (A-G): ").upper()) - ord('A')
            else:
                raise ValueError("Неверное направление")

            if is_valid_location(board, ship, direction, row, col):
                if direction == 'v':
                    for i in range(len(ship)):
                        board[row + i][col] = 'O'
                elif direction == 'h':
                    for i in range(len(ship)):
                        board[row][col + i] = 'O'
                break
            else:
                print("Неверное расположение корабля. Попробуйте еще раз.")
        except (ValueError, IndexError):
            print("Неверный ввод. Попробуйте еще раз.")

def is_hit(board, row, col):
    return board[row][col] == 'O'

def update_board(board, row, col, result):
    if result == 'hit':
        board[row][col] = 'X'
    elif result == 'miss':
        board[row][col] = '-'

def is_ship_sunk(board, ship, row, col):
    for i in range(len(ship)):
        if not is_hit(board, row + i, col):
            return False
    return True

def play_battleship():
    player_name = input("Введите ваше имя: ")
    board_size = 7
    num_ships = {'1': 4, '2': 2, '3': 1}
    ships = ['111', '11', '11', '1']

    player_board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    computer_board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

    print(f"Привет, {player_name}! Давай разместим твои корабли.")

    for ship in ships:
        clear_screen()
        print_board(player_board)
        print(f"Размести корабль {len(ship)} палубы.")
        direction = input("Выбери направление (v - вертикально, h - горизонтально): ")
        place_ship(player_board, ship, direction)

    clear_screen()
    print(f"Отлично, {player_name}! Теперь начнем битву.")

    shots = 0

    while any(ship_count > 0 for ship_count in num_ships.values()):
        clear_screen()
        print_board(computer_board)

        try:
            if shots > 0:
                print(f"Количество бросков: {shots}")
            row = int(input("Введите номер строки (1-7): ")) - 1
            col = ord(input("Введите букву столбца (A-G): ").upper()) - ord('A')
        except (ValueError, IndexError):
            print("Неверный ввод. Попробуйте еще раз.")
            continue

        if computer_board[row][col] == ' ':
            result = 'miss'
        elif computer_board[row][col] == 'O':
            result = 'hit'
            for ship_size, ship_count in num_ships.items():
                if ship_count > 0 and is_ship_sunk(computer_board, ship_size * ship_count, row, col):
                    num_ships[ship_size] -= 1
                    print(f"Корабль {ship_size} палубы потоплен!")
        else:
            print("Вы уже стреляли по этой клетке. Попробуйте другую.")
            continue

        shots += 1
        update_board(computer_board, row, col, result)

    clear_screen()
    print(f"Поздравляем, {player_name}! Вы выиграли за {shots} бросков!")

if __name__ == "__main__":
    play_battleship()



     

      
