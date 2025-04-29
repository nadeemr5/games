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
import random

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there's a winner."""
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != "-":
            return row[0]

    # Check columns
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != "-":
            return board[0][col]

    # Check diagonals
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != "-":
        return board[0][0]
    if len(set([board[i][2 - i] for i in range(3)])) == 1 and board[0][2] != "-":
        return board[0][2]

    return None

def player_input(board, player):
    """Get player's input and update the board."""
    while True:
        try:
            position = int(input(f"Player {player}, enter a position (1-9): "))
            if 1 <= position <= 9:
                row = (position - 1) // 3
                col = (position - 1) % 3
                if board[row][col] == "-":
                    board[row][col] = player
                    return
                else:
                    print("Position already taken. Try again.")
            else:
                print("Invalid position. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_input(board, player):
    """Computer's move."""
    available_positions = [(row, col) for row in range(3) for col in range(3) if board[row][col] == "-"]
    position = random.choice(available_positions)
    board[position[0]][position[1]] = player

def initialize_board():
    """Initialize the Tic Tac Toe board."""
    return [["-" for _ in range(3)] for _ in range(3)]

def play_game():
    """Play Tic Tac Toe."""
    print("Welcome to Tic Tac Toe!")
    print_board([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
    board = initialize_board()
    players = ["X", "O"]
    turn = 0

    while True:
        player = players[turn % 2]
        if player == "X":
            player_input(board, player)
        else:
            computer_input(board, player)

        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        elif "-" not in [position for row in board for position in row]:
            print("It's a tie!")
            break

        turn += 1

if __name__ == "__main__":
    play_game()
