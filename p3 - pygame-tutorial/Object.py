from pygame import *
from pygame.sprite import *


class Object(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, 200, 200)
    
    def update(self):
        pass
    
    def move(self, pos):
        self.rect.move_ip(pos)