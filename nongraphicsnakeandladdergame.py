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

# Define the game board with snakes and ladders
snakes_and_ladders = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

# Function to roll a die
def roll_die():
    return random.randint(1, 6)

# Function to move the player
def move_player(current_position, die_roll):
    new_position = current_position + die_roll
    if new_position in snakes_and_ladders:
        print("Oops! You landed on a snake or ladder!")
        new_position = snakes_and_ladders[new_position]
    return new_position

# Function to check if the player has won
def has_won(position):
    return position >= 100

# Function to draw the game board
def draw_board(player1_position, player2_position):
    for row in range(10, 0, -1):
        for col in range(1, 11):
            square_number = (row - 1) * 10 + col
            if square_number == player1_position:
                print("P1", end="\t")
            elif square_number == player2_position:
                print("P2", end="\t")
            else:
                print(square_number, end="\t")
        print()

# Main function to run the game
def play_snakes_and_ladders():
    player1_position = 0
    player2_position = 0
    current_player = 1
    while True:
        input("Press Enter to roll the die for Player " + str(current_player) + "...")
        die_roll = roll_die()
        print("Player " + str(current_player) + " rolled a", die_roll)
        if current_player == 1:
            player1_position = move_player(player1_position, die_roll)
            print("Player 1's new position is", player1_position)
            if has_won(player1_position):
                print("Player 1 wins!")
                break
            current_player = 2
        else:
            player2_position = move_player(player2_position, die_roll)
            print("Player 2's new position is", player2_position)
            if has_won(player2_position):
                print("Player 2 wins!")
                break
            current_player = 1
        draw_board(player1_position, player2_position)

# Start the game
play_snakes_and_ladders()
