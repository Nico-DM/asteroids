import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.time_until_next_shot = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius # type: ignore
        b = self.position - forward * self.radius - right # type: ignore
        c = self.position - forward * self.radius + right # type: ignore
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # type: ignore
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.time_until_next_shot <= 0:
            self.time_until_next_shot = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position[0], self.position[1])
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]: # W or UP = move forward
            self.move(dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: # A or LEFT = rotate counterclockwise
            self.rotate(-dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: # S or DOWN = move backwards
            self.move(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # D or RIGHT = rotate clockwise
            self.rotate(dt)
        if keys[pygame.K_SPACE]: # SPACE = shoot
            self.shoot()
        
        if self.time_until_next_shot > 0:
            self.time_until_next_shot -= dt