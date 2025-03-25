from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.speed = 0
        self.direction = pygame.Vector2(0, 1).rotate(self.rotation)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
    