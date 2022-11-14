import pygame.draw
import random

from Entity import Entity


class Ant(Entity):
    def __init__(self, x, y, scale, screen, ttl=100, width=80, height=60):
        super().__init__(x, y, scale, screen, width, height)
        self.color = "black"
        self.ttl = ttl

    def generate_movement(self):
        self.x += random.randint(-1, 1)
        if self.x <= 0:
            self.x = 1
        if self.x >= self.width:
            self.x = self.width - 1
        self.y += random.randint(-1, 1)
        if self.y <= 0:
            self.y = 1
        if self.y >= self.height:
            self.y = self.height - 1

    def update(self):
        # generate random movement
        self.generate_movement()
        self.draw()
