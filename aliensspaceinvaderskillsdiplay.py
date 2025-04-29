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
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 20
player_speed = 5

# Alien settings
alien_width = 50
alien_height = 50
alien_speed = 2

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 7

# Create the player
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Lists to hold aliens and bullets
aliens = []
bullets = []

# Font for displaying text
font = pygame.font.SysFont(None, 30)

def draw_window(alien_kills):
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, player)
    for alien in aliens:
        pygame.draw.rect(window, RED, alien)
    for bullet in bullets:
        pygame.draw.rect(window, WHITE, bullet)

    # Display alien kills on the screen
    text = font.render("Alien Kills: " + str(alien_kills), True, WHITE)
    window.blit(text, (10, 10))

    pygame.display.update()

def move_aliens():
    for alien in aliens:
        alien.y += alien_speed

def move_bullets():
    for bullet in bullets:
        bullet.y -= bullet_speed

def main():
    clock = pygame.time.Clock()
    running = True
    alien_kills = 0

    while running:
        clock.tick(60)  # 60 frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running to False to exit the loop
                break  # Exit the event loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player.x + player.width // 2 - bullet_width // 2, player.y, bullet_width, bullet_height)
                    bullets.append(bullet)

        if not running:
            break  # Exit the main loop if running is False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x + player.width < WIDTH:
            player.x += player_speed

        # Spawn new aliens randomly
        if random.randint(1, 100) == 1:
            alien_x = random.randint(0, WIDTH - alien_width)
            alien_y = -alien_height
            alien = pygame.Rect(alien_x, alien_y, alien_width, alien_height)
            aliens.append(alien)

        move_aliens()
        move_bullets()

        # Check for collisions between bullets and aliens
        for bullet in bullets:
            for alien in aliens:
                if bullet.colliderect(alien):
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    alien_kills += 1

        draw_window(alien_kills)

    pygame.quit()

if __name__ == "__main__":
    main()
