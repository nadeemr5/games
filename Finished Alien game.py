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
from pygame.sprite import Sprite

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 1.0
        self.bullets_allowed = 3  # Maximum number of bullets allowed on screen

        # Alien settings
        self.alien_width = 40
        self.alien_height = 40
        self.alien_color = (0, 0, 255)
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/Users/Adnaan/Documents/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen.get_rect().midbottom

        # Store a decimal value for the ship's horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen.get_rect().bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
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

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Create an alien at (0, 0) and then set the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.alien_width, self.settings.alien_height)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = self.settings.alien_color

    def update(self):
        """Move the alien to the right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def draw_alien(self):
        """Draw the alien to the screen."""
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.settings.alien_width // 2)

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
            self.bullets = pygame.sprite.Group()
            self.aliens = pygame.sprite.Group()

            self._create_fleet()
            self.kills = 0
            self.font = pygame.font.Font(None, 36)
        except pygame.error as e:
            traceback.print_exc()
            sys.exit()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create the first row of aliens.
        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
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

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for collisions between bullets and aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.kills += len(collisions)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            alien.draw_alien()

        # Display kill count
        kills_text = self.font.render(f"Kills: {self.kills}", True, (255, 255, 255))
        self.screen.blit(kills_text, (10, 10))

        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        try:
            while True:
                self._check_events()
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()
        except Exception as e:
            traceback.print_exc()
        finally:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
