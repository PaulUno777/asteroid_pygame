import pygame
import random
from circle_shape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        
        direction1 = self.velocity.rotate(random_angle)
        direction2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        random_speed = random.uniform(1, 1.5)

        asteroid1.velocity = direction1 * random_speed
        random_speed = random.uniform(1, 1.5)
        asteroid2.velocity = direction2 * random_speed
        
        