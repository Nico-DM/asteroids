import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        vector_cw = self.velocity.rotate(random_angle)
        vector_ccw = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_cw = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_ccw = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_cw.velocity = vector_cw * 1.2
        asteroid_ccw.velocity = vector_ccw * 1.2