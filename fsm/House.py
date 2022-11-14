from pygame import *

from Entity import Entity


class House(Entity):
    def __init__(self, x, y, scale, screen, width=80, height=60):
        super().__init__(x, y, scale, screen, width, height)
        self.color = "green"
