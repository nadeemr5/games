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

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"


# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# Take player input
def playerInput(board):
    while True:
        player = input("Enter a number from 1-9: ")
        if player.isdigit():
            player = int(player)
            if 1 <= player <= 9 and board[player - 1] == "-":
                board[player - 1] = currentPlayer
                return True  # Return True if input is valid and position is available
            else:
                print("Invalid selection or position in use")
        else:
            print("Invalid input. Please enter a number.")


# Check for winner or tie
def checkWinner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != "-":
            return board[i]  # Return the winning player
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != "-":
            return board[i]  # Return the winning player
    if board[0] == board[4] == board[8] != "-":
        return board[0]  # Return the winning player
    if board[2] == board[4] == board[6] != "-":
        return board[2]  # Return the winning player
    # Check for a tie
    if "-" not in board:
        return "Tie"  # Return "Tie" if all positions are filled
    return None  # Return None if the game is still ongoing


# Game loop
while True:
    printBoard(board)
    valid_input = False
    while not valid_input:
        valid_input = playerInput(board)
    winner = checkWinner(board)
    if winner:
        printBoard(board)
        if winner == "Tie":
            print("It's a tie!")
        else:
            print(f"The winner is {winner}!")
        break  # Exit the game loop if there's a winner or a tie
    currentPlayer = "O" if currentPlayer == "X" else "X"  # Switch players

