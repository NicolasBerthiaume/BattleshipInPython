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
            print("Ship cannot fit horizontally.")
            return False
    
        for col in range(start_col, start_col + ship.size):
            if board[start_row][col] != '~':
                print("Space is already occupied.")
                return False
        
        for col in range(start_col, start_col + ship.size):
            board[start_row][col] = 'S'
        
        return True

    elif orientation == 'v':
        if start_row + ship.size > len(board[0]):
            print("Ship cannot fit vertically.")
            return False
        
        for row in range(start_row, start_row + ship.size):
            if board[row][start_col] != '~':
                print("Space is already occupied.")
                return False
            
        for row in range(start_row, start_row + ship.size):
            board[row][start_col] = 'S'
        
        return True
    
    else:
        print("Invalid orientation.")
        return False

def prompt_user_to_place_ship(ship):
    while True:
        print(f"\nPlace your {ship.name} (Size: {ship.size}):")
        ship_col = int(input(f"Which column will you place the {ship.name} on? "))
        ship_row = int(input(f"Which row will you place the {ship.name} on? "))
        ship_orient = input(f"Will you place your {ship.name} horizontally (h) or vertically (v)? ").lower()

        if place_ship(player_board, ship, (ship_row, ship_col), ship_orient):
            print(f"{ship.name} placed successfully!")
            print("\n")
            print_board(player_board)
            break
        else:
            print(f"Invalid placement for {ship.name}. Try again.")

# the game loop starts here

print("\n")
print("Welcome to Battleship, Player!")
print("How big do you want the board to be?")

while True:
    try:
        boardsize = int(input("Enter a number between 5 and 10: "))
        if 5 < boardsize < 10:
            break
        else:
            print("Invalid size. Please enter a number better 5 and 10.")
    except ValueError:
        ("Invalid input. Please enter a valid integer.")

print("You entered the number " + str(boardsize))

CPU_board = create_grid(boardsize)
player_board = create_grid(boardsize)

print("\n")
print("Here is your board:")
print("\n")

print_board(player_board)

prompt_user_to_place_ship(player_big_ship)
prompt_user_to_place_ship(player_med_ship)
prompt_user_to_place_ship(player_small_ship)