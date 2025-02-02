import sys
import pygame
import random
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from star import Star

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     game_clock = pygame.time.Clock()
#     dt = 0

#     updatable = pygame.sprite.Group()
#     drawable = pygame.sprite.Group()
#     asteroids = pygame.sprite.Group()
#     shots = pygame.sprite.Group()

#     Player.containers = (updatable, drawable)
#     Asteroid.containers = (asteroids, updatable, drawable)
#     AsteroidField.containers = (updatable)
#     Shot.containers = (shots, updatable, drawable)
#     player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     asteroid_field = AsteroidField()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return
            
#             elif event.type == pygame.VIDEORESIZE:
#                 # Handle window resizing
#                 screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
#                 current_screen_width, current_screen_height = event.size
#                 player.update_screen_size(current_screen_width, current_screen_height)
#                 asteroid_field.update_screen_size(current_screen_width, current_screen_height)
#                 for a in asteroids:
#                     a.update_screen_size(current_screen_width, current_screen_height)
        
#         for u in updatable:
#             u.update(dt)

#         for a in asteroids:
#             if a.has_collided(player):
#                 print("Game over!")
#                 sys.exit()
#             for shot in shots:
#                 if a.has_collided(shot):
#                     a.split()
#                     shot.kill()

#         screen.fill("black")

#         for d in drawable:
#             d.draw(screen)

#         pygame.display.flip()

#         # limit the framerate to 60 FPS
#         dt = game_clock.tick(60) / 1000

def main():
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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create player and asteroid field
    screen_width, screen_height = screen.get_size()
    player = Player(screen_width / 2, screen_height / 2)
    asteroid_field = AsteroidField()

    # Create stars
    stars_resizer = 1
    stars = [
        Star(random.randint(0, screen_width), random.randint(0, screen_height), random.randint(100, 255))
        for _ in range(100)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.VIDEORESIZE:
                stars_resizer = 3//stars_resizer
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                screen_width, screen_height = event.size
                player.update_screen_size(screen_width, screen_height)
                player.position = pygame.Vector2(screen_width / 2, screen_height / 2)
                asteroid_field.update_screen_size(screen_width, screen_height)
                for a in asteroids:
                    a.update_screen_size(screen_width, screen_height)
                stars = [
                    Star(random.randint(0, screen_width), random.randint(0, screen_height), random.randint(100, 255), screen_width, screen_height)
                    for _ in range(100 * stars_resizer)
                ]

        # Player movement offset
        keys = pygame.key.get_pressed()
        offset = pygame.Vector2(0, 0)
        if keys[pygame.K_w]:
            offset += player.forward_vector() * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            offset -= player.forward_vector() * PLAYER_SPEED * dt

        # Update all elements with the offset
        for u in updatable:
            u.update(dt)

        # Update stars with offset
        for star in stars:
            star.update(offset)

        # Check collisions
        for a in asteroids:
            a.position -= offset
            if a.has_collided(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if a.has_collided(shot):
                    a.split()
                    shot.kill()

        # Draw background
        screen.fill("black")
        for star in stars:
            star.draw(screen)

        # Draw all drawable elements
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
