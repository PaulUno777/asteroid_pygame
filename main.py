# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroid import Asteroid
from asteroid_field import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0

     # Create the two groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()

    Player.containers = updatable, drawable
    Asteroid.containers = updatable, drawable, asteroids
    AsteroidField.containers = updatable
    Shot.containers = updatable, drawable,player_shots
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        screen.fill((0, 0, 0))
        # Draw all drawable objects
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            for shot in player_shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()

        # Check for collisions
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                pygame.quit()
                return
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        delta_time = clock.tick(60) / 1000
        updatable.update(delta_time)


if __name__ == "__main__":
    main()

