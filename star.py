import pygame # type: ignore
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Star:
    """Represents a star in the background of the game."""

    def __init__(self, x, y, brightness, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT):
        """
        Initialize a star with position, brightness, and screen dimensions.

        Args:
            x (float): Initial x-coordinate.
            y (float): Initial y-coordinate.
            brightness (int): Intensity of the star's brightness (0-255).
            screen_width (int): Width of the game screen.
            screen_height (int): Height of the game screen.
        """
        self.position = pygame.Vector2(x, y)
        self.brightness = brightness
        self.color = random.choice([
            (self.brightness, self.brightness, self.brightness),  # White
            (self.brightness, self.brightness, self.brightness),  # White
            (self.brightness, self.brightness, self.brightness),  # White
            (self.brightness, self.brightness, self.brightness),  # White
            (200, 200, self.brightness),  # Blue-white
            (self.brightness, 200, 150),  # Yellow-white
            (self.brightness, 150, 100),  # Orange
            (self.brightness, 100, 100),  # Red
        ])
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    def update_screen_size(self, width, height):
        """Update the screen dimensions."""
        self.screen_width = width
        self.screen_height = height

    def draw(self, screen):
        """Draw the star on the screen."""
        pygame.draw.circle(screen, self.color, self.position, 1)

    def update(self, offset):
        """
        Update the star's position with wrapping around screen edges.

        Args:
            offset (Vector2): The amount to move the star.
        """
        self.position += offset
        # Wrap stars around the screen edges
        if self.position.x < 0:
            self.position.x += self.screen_width
        elif self.position.x > self.screen_width:
            self.position.x -= self.screen_width
        if self.position.y < 0:
            self.position.y += self.screen_height
        elif self.position.y > self.screen_height:
            self.position.y -= self.screen_height
