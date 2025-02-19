import random

def create_grid(gridsize):
    return [['~' for _ in range(gridsize)] for _ in range(gridsize)]

def print_board(board):
    print("   ", end="")
    for col in range(1, len(board[0]) + 1):
        print(col, end=" ")
    print()
    
    for row_num, row in enumerate(reversed(board), start = 1):
        print(f"{len(board) - row_num + 1:2} ", end="")
        print(' '.join(row))

class Ship():
    def __init__(self, name, size):
        self.name = name
        self.size = size

CPU_big_ship = Ship("Big Ship", 4)
CPU_med_ship = Ship("Medium Ship", 3)
CPU_small_ship = Ship("Small Ship", 2)

player_big_ship = Ship("Big Ship", 4)
player_med_ship = Ship("Medium Ship", 3)
player_small_ship = Ship("Small Ship", 2)

def place_ship(board, ship, start, orientation):
    
    start_row, start_col = start[0] -1, start[1] -1

    if orientation == 'h':
        if start_col + ship.size > len(board[0]):
            return False
    
        for col in range(start_col, start_col + ship.size):
            if board[start_row][col] != '~':
                return False
        
        for col in range(start_col, start_col + ship.size):
            board[start_row][col] = 'S'
        
        return True

    elif orientation == 'v':
        if start_row + ship.size > len(board[0]):
            return False
        
        for row in range(start_row, start_row + ship.size):
            if board[row][start_col] != '~':
                return False
            
        for row in range(start_row, start_row + ship.size):
            board[row][start_col] = 'S'
        
        return True
    
    else:
        return False

def prompt_user_to_select_board_size():
    print("How big do you want the board to be?")

    while True:
        try:
            boardsize = int(input("Enter a number between 5 and 10: "))
            if 5 <= boardsize <= 10:
                break
            else:
                print("Invalid size. Please enter a number better 5 and 10.")
        except ValueError:
            ("Invalid input. Please enter a valid integer.")

    print("You entered the number " + str(boardsize))

    return boardsize

def prompt_user_to_place_ship(board, ship):
    while True:
        print(f"\nPlace your {ship.name} (Size: {ship.size}):")
        ship_col = int(input(f"Which column will you place the {ship.name} on? "))
        ship_row = int(input(f"Which row will you place the {ship.name} on? "))
        ship_orient = input(f"Will you place your {ship.name} horizontally (h) or vertically (v)? ").lower()

        if place_ship(board, ship, (ship_row, ship_col), ship_orient):
            print(f"{ship.name} placed successfully!")
            print("\n")
            print_board(board)
            break
        else:
            print(f"Invalid placement for {ship.name}. Try again.")

def place_CPU_ships_at_random(board, ship):
    ship_placed = False

    while not ship_placed:
        start_row = random.randint(0, len(board) - 1)
        start_col = random.randint(0, len(board[0]) - 1)
        orientation = random.choice(['h', 'v'])

        if place_ship(board, ship, (start_row + 1, start_col + 1), orientation):
            ship_placed = True

def print_both_boards(CPU_hidden, player_open):
    print()
    print("CPU BOARD")
    print_board(CPU_hidden)
    print()
    print("PLAYER BOARD")
    print_board(player_open)
    print()

player_hits_counter = 0

def prompt_player_guess(hidden_board, guess_board, boardsize):
    global player_hits_counter
    print("What will be your move?")

    while True:
        guess_row = int(input(f"Enter the row (1 to {boardsize}): ")) - 1
        guess_col = int(input(f"Enter the column (1 to {boardsize}): ")) - 1

        if 0 <= guess_row < boardsize and 0 <= guess_col < boardsize:
            break
        else:
            print(f"Invalid guess. Please enter numbers between 1 and {boardsize}.")
    
    if hidden_board[guess_row][guess_col] == 'S':
        print("You hit a ship!")
        player_hits_counter += 1
        guess_board[guess_row][guess_col] = 'X'
    else:
        print("Sploosh! In the water...")
        guess_board[guess_row][guess_col] = 'O'

cpu_hits_counter = 0
cpu_previous_guesses = set()

def CPU_guess(board):
    global cpu_hits_counter
    global cpu_previous_guesses

    while True:
        guess_row = random.randint(0, len(board) - 1)
        guess_col = random.randint(0, len(board[0]) - 1)

        if (guess_row, guess_col) not in cpu_previous_guesses:
            cpu_previous_guesses.add((guess_row, guess_col))
            break

    print(f"CPU guesses... Row: {guess_row + 1}, Column: {guess_col + 1}")
    if board[guess_row][guess_col] == 'S':
        print("CPU hit your ship!")
        cpu_hits_counter += 1
        board[guess_row][guess_col] = 'X'
    else:
        print("CPU missed!")

# the game loop starts here

print("\n")
print("Welcome to Battleship, Player!")
print("\n")

CPU_board = create_grid(prompt_user_to_select_board_size())
player_board = create_grid(len(CPU_board[0]))
guess_board = create_grid(len(CPU_board[0]))

print("\n")
print("Here is your board:")
print("\n")

print_board(player_board)

place_CPU_ships_at_random(CPU_board, CPU_big_ship)
place_CPU_ships_at_random(CPU_board, CPU_med_ship)
place_CPU_ships_at_random(CPU_board, CPU_small_ship)

prompt_user_to_place_ship(player_board, player_big_ship)
prompt_user_to_place_ship(player_board, player_med_ship)
prompt_user_to_place_ship(player_board, player_small_ship)

print("\nWe're ready to play!")

player_hits_to_win = player_big_ship.size + player_med_ship.size + player_small_ship.size
CPU_hits_to_win = CPU_big_ship.size + CPU_med_ship.size + CPU_small_ship.size

def play_to_win():
    while player_hits_counter < player_hits_to_win and cpu_hits_counter < CPU_hits_to_win:
        print_both_boards(guess_board, player_board)
        prompt_player_guess(CPU_board, guess_board, len(CPU_board[0]))
        CPU_guess(player_board)

    winner = ""

    print_both_boards(guess_board, player_board)

    if player_hits_counter == player_hits_to_win:
        winner = "Player has won!"
    else:
        winner = "CPU has won!"
    
    return winner

print(play_to_win())

