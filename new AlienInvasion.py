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
import traceback

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800  # Adjusted screen width
        self.screen_height = 600  # Adjusted screen height
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 1.0

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        try:
            self.image = pygame.image.load('C:/Users/Adnaan/Documents/ship.bmp')
            self.rect = self.image.get_rect()
        except pygame.error as e:
            traceback.print_exc()
            sys.exit()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1  # Adjust the value for faster or slower movement
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1  # Adjust the value for faster or slower movement
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1  # Adjust the value for faster or slower movement
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1  # Adjust the value for faster or slower movement

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

class Bullet:
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        try:
            pygame.init()
            self.settings = Settings()

            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
            pygame.display.set_caption("Alien Invasion")

            self.ship = Ship(self)
            self.bullets = []  # List to store bullets
        except pygame.error as e:
            traceback.print_exc()
            sys.exit()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_UP:
                        self.ship.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.ship.moving_down = True
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    elif event.key == pygame.K_UP:
                        self.ship.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.ship.moving_down = False

            # Update the ship's position
            self.ship.update()

            # Update bullets
            for bullet in self.bullets:
                bullet.update()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Draw bullets
            for bullet in self.bullets:
                bullet.draw_bullet()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets list."""
        new_bullet = Bullet(self)
        self.bullets.append(new_bullet)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
