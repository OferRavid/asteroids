import pygame # type: ignore

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """Represents a circular shape with position, velocity, and radius."""

    def __init__(self, x, y, radius):
        """
        Initialize the circle's position, radius, and default velocity.

        Args:
            x (float): Initial x-coordinate.
            y (float): Initial y-coordinate.
            radius (int): Radius of the circle.
        """
        # If object has "containers" attribute, give it to super() for initialization
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def has_collided(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def kill(self):
        """Remove the circle from all sprite groups."""
        super().kill()
