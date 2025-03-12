import pygame # type: ignore
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    """Represents the player-controlled spaceship."""

    def __init__(self, x, y):
        """
        Initialize the player with position, rotation, and screen dimensions.

        Args:
            x (float): Initial x-coordinate.
            y (float): Initial y-coordinate.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def update_screen_size(self, width, height):
        """Update the screen dimensions."""
        self.screen_width = width
        self.screen_height = height

    def draw(self, screen):
        """Draw the player spaceship on the screen."""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        """
        Calculate the points of the spaceship's triangular shape.

        Returns:
            list[Vector2]: List of three points forming the triangle.
        """
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        """Rotate the player by a given amount over time."""
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def shoot(self):
        """Create a shot fired from the player's position."""
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
    
    def update(self, dt):
        """
        Update the player's state, handling movement and shooting.

        Args:
            dt (float): Time delta for frame update.
        """
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] and self.shot_timer <= 0:
            self.shoot()
    
    def forward_vector(self):
        """Get the forward direction vector of the player."""
        return pygame.Vector2(0, 1).rotate(self.rotation)
