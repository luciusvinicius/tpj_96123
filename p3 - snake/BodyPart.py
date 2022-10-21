from typing import Tuple, overload
from pygame import *
from pygame.sprite import *

IMG_URL = "./sprites/banana.jpg"
SPEED = 4

class BodyPart(Sprite):
    def __init__(self, x, y, direction, scale=0, speed=SPEED):
        Sprite.__init__(self)
        # self.x : int = x-35
        # self.y : int = y-18
        self.x : int = x
        self.y : int = y
        self.rect = Rect(self.x, self.y, 1, 1)
        self.prev : BodyPart = None
        self.next : BodyPart = None
        self.direction : Tuple = direction
        # self.scale = scale
        
        picture = image.load(IMG_URL)
        picture = transform.scale(picture, (1, 1)) # scale
        self.image = picture.convert_alpha()
        
    def move(self, pos):
        self.rect.move_ip((pos[0] * self.rect.width * SPEED, pos[1] * self.rect.height * SPEED))
        # print(self.rect)
        # print(self.scale)
        self.x += pos[0]*SPEED
        self.y += pos[1]*SPEED
        
    def __str__(self):
        return f"BodyPart: ({self.rect.x}, {self.rect.y})"
    
    # @move.overload
    # def move(self, x, y):
    #     self.rect.move_ip(x, y)