def create_grid(gridsize):
    return ['~' * gridsize for _ in range(gridsize)]

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
    
    start_row, start_col = start

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

size = 5
board = create_grid(size)
print(f'creating a {size}x{size} board')

for row in board:
    print(' '.join(row))

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

for row in player_board:
    print(' '.join(row))

