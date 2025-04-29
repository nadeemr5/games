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
pygame.display.set_caption("Sprites and Collision Detection Tutorial")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Green color for the player
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  # Red color for the enemy
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Example enemy creation
enemy = Enemy(200, 200)
all_sprites.add(enemy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    all_sprites.update()

    # Collision detection
    hits = pygame.sprite.spritecollide(player, all_sprites, False)
    if hits:
        # Handle collision (e.g., player loses a life)
        print("Collision detected!")

    # Draw
    screen.fill((255, 255, 255))  # White background
    all_sprites.draw(screen)

    pygame.display.flip()
