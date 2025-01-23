import random
import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, screen_width, screen_height):
        super().__init__(x, y, radius)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update_screen_size(self, width, height):
        self.screen_width = width
        self.screen_height = height
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.edge_wrap()
    
    def split(self):
        old_velocity = self.velocity
        old_radius = self.radius
        old_position = self.position
        old_screen_width = self.screen_width
        old_screen_height = self.screen_height
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        right_velocity = old_velocity.rotate(random_angle)
        left_velocity = old_velocity.rotate(-random_angle)
        radius = old_radius - ASTEROID_MIN_RADIUS
        right_asteroid = Asteroid(old_position.x, old_position.y, radius, old_screen_width, old_screen_height)
        right_asteroid.velocity = right_velocity * 1.2
        left_asteroid = Asteroid(old_position.x, old_position.y, radius, old_screen_width, old_screen_height)
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
