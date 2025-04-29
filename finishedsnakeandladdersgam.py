#-------------------------------------------------------------------------------
# Name:        module2
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
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and Ladders")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define font
font = pygame.font.SysFont(None, 36)

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
        new_position = snakes_and_ladders[new_position]
    return new_position

# Function to draw the game board
def draw_board(player1_position, player2_position):
    screen.fill(WHITE)
    for row in range(10):
        for col in range(10):
            square_number = row * 10 + col + 1
            pygame.draw.rect(screen, BLUE, (col * 60, row * 60, 60, 60), 2)
            text = font.render(str(square_number), True, RED)
            screen.blit(text, (col * 60 + 20, row * 60 + 20))
    # Draw player1
    pygame.draw.circle(screen, RED, (player1_position % 10 * 60 + 30, HEIGHT - (player1_position // 10 * 60 + 30)), 20)
    # Draw player2
    pygame.draw.circle(screen, BLUE, (player2_position % 10 * 60 + 30, HEIGHT - (player2_position // 10 * 60 + 30)), 20)
    pygame.display.flip()

# Main function to run the game
def play_snakes_and_ladders():
    player1_position = 0
    player2_position = 0
    current_player = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                die_roll = roll_die()
                if current_player == 1:
                    player1_position = move_player(player1_position, die_roll)
                    current_player = 2  # Switch to player 2
                else:
                    player2_position = move_player(player2_position, die_roll)
                    current_player = 1  # Switch to player 1
                draw_board(player1_position, player2_position)

# Start the game
play_snakes_and_ladders()
