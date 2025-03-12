import pygame # type: ignore
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    """A projectile shot by the player."""

    def __init__(self, x, y):
        """Initialize a shot at (x, y)."""
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        """Draw the shot as a white circle."""
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        """Move the shot based on velocity and time step."""
        self.position -= self.velocity * dt
