import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Star:
    def __init__(self, x, y, brightness, screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT):
        self.position = pygame.Vector2(x, y)
        self.brightness = brightness  # Determines the intensity of the star (color depth)
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
        self.screen_width = width
        self.screen_height = height

    def draw(self, screen):
        # color = (self.brightness, self.brightness, self.brightness)
        pygame.draw.circle(screen, self.color, self.position, 1)

    def update(self, offset):
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
