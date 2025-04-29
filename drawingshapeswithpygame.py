#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adnaan
#
# Created:     16/02/2024
# Copyright:   (c) Adnaan 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drawing Shapes Tutorial")

# Set colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
purple = (128, 0, 128)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white color
    screen.fill(white)

    # Draw a rectangle
    pygame.draw.rect(screen, blue, (100, 100, 50, 50))

    # Draw a red circle
    pygame.draw.circle(screen, red, (200, 200), 30)

    # Draw a purple polygon
    pygame.draw.polygon(screen, purple, [(500, 500), (600, 550), (650, 500), (600, 450)])

    # Draw a line
    pygame.draw.line(screen, (255, 0, 0), (300, 100), (400, 200), 5)

    # Draw an ellipse
    pygame.draw.ellipse(screen, (0, 255, 0), (400, 300, 100, 50), 2)

    # Draw an arc
    pygame.draw.arc(screen, (255, 255, 0), (100, 300, 100, 50), 0, 3.14, 2)

    # Render text
    font = pygame.font.Font(None, 36)
    text_surface = font.render('Pygame Shapes', True, (0, 0, 0))
    screen.blit(text_surface, (200, 50))

    # Draw a filled circle
    pygame.draw.circle(screen, (0, 255, 255), (500, 200), 30)

    # Draw a Bezier curve
    pygame.draw.aalines(screen, (255, 0, 255), False, [(600, 100), (700, 200), (750, 100)], 1)

    # Update the display
    pygame.display.update()






