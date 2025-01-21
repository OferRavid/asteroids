import random
import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        old_velocity = self.velocity
        old_radius = self.radius
        old_position = self.position
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        right_velocity = old_velocity.rotate(random_angle)
        left_velocity = old_velocity.rotate(-random_angle)
        radius = old_radius - ASTEROID_MIN_RADIUS
        right_asteroid = Asteroid(old_position.x, old_position.y, radius)
        right_asteroid.velocity = right_velocity * 1.2
        left_asteroid = Asteroid(old_position.x, old_position.y, radius)
        left_asteroid.velocity = left_velocity * 1.2
