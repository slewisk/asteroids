from circleshape import CircleShape
from constants import *
import pygame, random

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
    
    def split(self):
        old_radius = self.radius
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        for i in range(2):
            asteroid = Asteroid(self.position.x, self.position.y, (old_radius - ASTEROID_MIN_RADIUS))
            if i == 0:
                asteroid.velocity = self.velocity.rotate(angle)
            else:
                asteroid.velocity = self.velocity.rotate(-angle)
            asteroid.speed = self.speed * 1.2