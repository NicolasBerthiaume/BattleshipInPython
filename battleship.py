import random

def create_grid(gridsize):
    return [['~' for _ in range(gridsize)] for _ in range(gridsize)]

def print_board(board):
    for row in reversed(board):
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

# the game loop starts here

print("\n")
print("Welcome to Battleship, Player!")
print("\n")

CPU_board = create_grid(prompt_user_to_select_board_size())
player_board = create_grid(len(CPU_board[0]))

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