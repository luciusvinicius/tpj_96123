import pygame.draw
import random

from Entity import Entity


class Ant(Entity):
    def __init__(self, x, y, scale, screen, ttl=100, width=80, height=60, spawners=None):
        super().__init__(x, y, scale, screen, width, height)
        if spawners is None:
            self.spawners = []
        else:
            self.spawners = spawners
        self.color = "black"
        self.ttl = ttl
        self.carried_obj = None

    def generate_movement(self):
        if self.carried_obj is None:
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

    # Check collision with a resource and get it
    def check_collision(self, spawner):
        if self.carried_obj is not None:
            return

        for entity in spawner.entities:
            if entity.x == self.x and entity.y == self.y:
                self.carried_obj = entity
                spawner.entities.remove(entity)
                return




    def update(self):
        # generate random movement
        self.generate_movement()
        self.draw()

