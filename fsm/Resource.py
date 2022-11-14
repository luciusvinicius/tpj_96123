import random
from Entity import Entity


def generate_position(width, height):
    x = random.randint(0, width)
    y = random.randint(0, height)
    return x, y

class Resource(Entity):
    def __init__(self, scale, screen, width=80, height=60):
        x, y = generate_position(width, height)
        super().__init__(x, y, scale, screen, width, height)
        self.color = "red"

    def update(self):
        self.draw()