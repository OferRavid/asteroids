"""
main.py - Handles the logic for running the Asteroids game.
"""
import sys
import pygame # type: ignore
import random
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from star import Star

def main():
    """
    Main game loop for the Asteroids game.

    Initializes Pygame, sets up the screen, creates game objects, and handles the main event loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    game_clock = pygame.time.Clock()
    dt = 0

    # Initialize sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    stars = pygame.sprite.Group()

    # Assign sprite groups to classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create player and asteroid field
    screen_width, screen_height = screen.get_size()
    player = Player(screen_width / 2, screen_height / 2)
    asteroid_field = AsteroidField()

    # Create stars for the background
    stars = [
        Star(random.randint(0, screen_width), random.randint(0, screen_height), random.randint(100, 255))
        for _ in range(250)
    ]

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop
            elif event.type == pygame.VIDEORESIZE:
                # Adjust screen size and elements when window is resized
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                screen_width, screen_height = event.size
                player.update_screen_size(screen_width, screen_height)
                player.position = pygame.Vector2(screen_width / 2, screen_height / 2)
                asteroid_field.update_screen_size(screen_width, screen_height)
                for a in asteroids:
                    a.update_screen_size(screen_width, screen_height)
                stars = [
                    Star(random.randint(0, screen_width), random.randint(0, screen_height), random.randint(100, 255), screen_width, screen_height)
                    for _ in range(random.choice([250, 500, 750]))
                ]

        # Calculate movement offset based on player input
        keys = pygame.key.get_pressed()
        offset = pygame.Vector2(0, 0)
        if keys[pygame.K_w]:
            offset += player.forward_vector() * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            offset -= player.forward_vector() * PLAYER_SPEED * dt

        # Update all updatable game objects
        for u in updatable:
            u.update(dt)

        # Update star positions with player movement offset
        for star in stars:
            star.update(offset)

        # Check for collisions between asteroids and player or shots
        for a in asteroids:
            a.position += offset
            if a.has_collided(player):
                print("Game over!")
                sys.exit()  # End game on collision with player
            for shot in shots:
                if a.has_collided(shot):
                    a.split()  # Split asteroid on collision
                    shot.kill()  # Remove shot on collision

        # Draw background and stars
        screen.fill("black")
        for star in stars:
            star.draw(screen)

        # Draw all drawable game elements
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()  # Update the display
        dt = game_clock.tick(60) / 1000  # Maintain 60 FPS

if __name__ == "__main__":
    main()
