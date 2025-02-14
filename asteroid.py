import random
import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, screen_width, screen_height, color=None):
        super().__init__(x, y, radius)
        self.screen_width = screen_width
        self.screen_height = screen_height
        if color != None:
            self.color = color
        else:
            self.color = random.choice([
                (255, 255, 255),  # White
                (255, 255, 255),  # White
                (255, 255, 255),  # White
                (255, 255, 255),  # White
                (200, 200, 255),  # Blue-white
                (255, 200, 150),  # Yellow-white
                (255, 150, 100),  # Orange
                (255, 100, 100),  # Red
            ])

    def update_screen_size(self, width, height):
        self.screen_width = width
        self.screen_height = height
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.edge_wrap()
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        right_velocity = self.velocity.rotate(random_angle)
        left_velocity = self.velocity.rotate(-random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        right_asteroid = Asteroid(self.position.x, self.position.y, radius, self.screen_width, self.screen_height, self.color)
        right_asteroid.velocity = right_velocity * 1.2
        left_asteroid = Asteroid(self.position.x, self.position.y, radius, self.screen_width, self.screen_height, self.color)
        left_asteroid.velocity = left_velocity * 1.2
    
    def edge_wrap(self):
        if self.position.x < -self.radius:
            self.position.x = self.screen_width + self.radius
        elif self.position.x > self.screen_width + self.radius:
            self.position.x = -self.radius

        if self.position.y < -self.radius:
            self.position.y = self.screen_height + self.radius
        elif self.position.y > self.screen_height + self.radius:
            self.position.y = -self.radius
