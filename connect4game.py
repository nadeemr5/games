#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adnaan
#
# Created:     15/02/2024
# Copyright:   (c) Adnaan 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# Define constants for the board size
ROWS = 6
COLUMNS = 7

def create_board():
    """Create an empty Connect 4 board."""
    return [["-" for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Print the Connect 4 board."""
    for row in board:
        print("|".join(row))
    print("-" * (COLUMNS * 2 - 1))

def drop_piece(board, col, player):
    """Drop a piece into the specified column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == "-":
            board[row][col] = player
            return True
    return False

def check_winner(board, player):
    """Check if the specified player has won."""
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

def is_board_full(board):
    """Check if the board is full."""
    return all(piece != "-" for row in board for piece in row)

def main():
    """Main function to run the Connect 4 game."""
    print("Welcome to Connect 4!")
    board = create_board()
    current_player = "X"

    while True:
        print_board(board)
        col = int(input(f"Player {current_player}, choose a column (1-{COLUMNS}): ")) - 1

        if col < 0 or col >= COLUMNS:
            print("Invalid column. Please choose again.")
            continue

        if not drop_piece(board, col, current_player):
            print("Column is full. Please choose another column.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
