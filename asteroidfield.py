import pygame # type: ignore
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    """
    Represents a field of asteroids, managing their spawning and screen resizing.
    """

    def __init__(self):
        """
        Initialize the asteroid field with spawn timing and screen dimensions.
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    @property
    def edges(self):
        """
        Define the screen edges for asteroid spawning along with their directions.

        Returns:
            list: A list of tuples containing direction vectors and spawn position lambdas.
        """
        return [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * self.screen_height),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    self.screen_width + ASTEROID_MAX_RADIUS, y * self.screen_height
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(x * self.screen_width, -ASTEROID_MAX_RADIUS),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    x * self.screen_width, self.screen_height + ASTEROID_MAX_RADIUS
                ),
            ],
        ]

    def update_screen_size(self, width, height):
        """
        Update the screen dimensions.
        """
        self.screen_width = width
        self.screen_height = height

    def spawn(self, radius, position, velocity):
        """
        Spawn a new asteroid with the given size, position, and velocity.

        Args:
            radius (int): The radius of the asteroid.
            position (pygame.Vector2): The initial position of the asteroid.
            velocity (pygame.Vector2): The movement velocity of the asteroid.
        """
        asteroid = Asteroid(position.x, position.y, radius, self.screen_width, self.screen_height)
        asteroid.velocity = velocity

    def update(self, dt):
        """
        Update the asteroid field by spawning asteroids at regular intervals.

        Args:
            dt (float): Delta time since the last frame, used to control spawn timing.
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge if there are less than ASTEROIDS_MAX_SPAWN asteroids
            if len(Asteroid.containers[0]) < ASTEROIDS_MAX_SPAWN:
                edge = random.choice(self.edges)
                speed = random.randint(40, 100)
                velocity = edge[0] * speed
                velocity = velocity.rotate(random.randint(-30, 30))
                position = edge[1](random.uniform(0, 1))
                kind = random.randint(1, ASTEROID_KINDS)
                self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
