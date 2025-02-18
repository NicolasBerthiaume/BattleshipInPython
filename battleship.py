def create_grid(gridsize):
    return [['~' for _ in range(gridsize)] for _ in range(gridsize)]

def print_board(board):
    for row in reversed(board):
        print(' '.join(row))

class Ship():
    def __init__(self, size):
        self.size = size

CPU_big_ship = Ship(4)
CPU_med_ship = Ship(3)
CPU_small_ship = Ship(2)

player_big_ship = Ship(4)
player_med_ship = Ship(3)
player_small_ship = Ship(2)

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

print("\n")
print("Now start placing your ships!")
print("Start with the big ship (4 spaces).")    

ship1_col = int(input("Which column will you place it on? "))
ship1_row = int(input("WHich row will you place it on? "))
ship1_orient = input("Will you place is horizontally (h) or vertically (v)? ").lower()

place_ship(player_board, player_big_ship, (ship1_row, ship1_col), ship1_orient)

print("\n")
print("Here is your board:")
print("\n")

print_board(player_board)

print("\n")
print("Now let's place the medium ship (3 spaces).")
ship2_col = int(input("Which column will you place it on? "))
ship2_row = int(input("WHich row will you place it on? "))
ship2_orient = input("Will you place is horizontally (h) or vertically (v)? ").lower()

place_ship(player_board, player_med_ship, (ship2_row, ship2_col), ship2_orient)

print("\n")
print("Here is your board:")
print("\n")

print_board(player_board)

print("\n")
print("Now let's place the small ship (2 spaces).")
ship3_col = int(input("Which column will you place it on? "))
ship3_row = int(input("WHich row will you place it on? "))
ship3_orient = input("Will you place is horizontally (h) or vertically (v)? ").lower()

place_ship(player_board, player_small_ship, (ship3_row, ship3_col), ship3_orient)

print("\n")
print("Here is your board:")
print("\n")

print_board(player_board)