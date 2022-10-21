import random
from pygame import *
from pygame.sprite import *

IMG_URL = "./sprites/banana.jpg"

class Food(Sprite):
    def __init__(self, WIDTH, HEIGHT):
        Sprite.__init__(self)
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        # self.SCALE = SCALE
        picture = image.load(IMG_URL)
        picture = transform.scale(picture, (1, 1)) # scale
        self.image = picture.convert_alpha()
        self.rect = None
        self.sprite = Group()
        self.change_position()
        self.sprite.add(self)
        
        
    def get_random_pos(self):
        return (random.randrange(self.WIDTH), random.randrange(self.HEIGHT))
        # return (random.randrange(self.WIDTH) * self.SCALE, random.randrange(self.HEIGHT) * self.SCALE)
    
        
    def change_position(self):
        random_pos = self.get_random_pos()
        self.rect = Rect(random_pos[0], random_pos[1], 1, 1)
        


        