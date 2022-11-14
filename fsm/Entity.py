import pygame.draw

class Entity:
    def __init__(self, x, y, scale, screen, width=80, height=60):
        self.x = x
        self.y = y
        self.scale = scale
        self.screen = screen
        self.height = height
        self.width = width
        self.color = "black"

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x * self.scale, self.y * self.scale, self.scale, self.scale))

    def update(self):
        self.draw()