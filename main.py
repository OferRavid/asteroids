import sys
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            elif event.type == pygame.VIDEORESIZE:
                # Handle window resizing
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                current_screen_width, current_screen_height = event.size
                player.update_screen_size(current_screen_width, current_screen_height)
                asteroid_field.update_screen_size(current_screen_width, current_screen_height)
                for a in asteroids:
                    a.update_screen_size(current_screen_width, current_screen_height)
        
        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.has_collided(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if a.has_collided(shot):
                    a.split()
                    shot.kill()

        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
