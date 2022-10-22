import random
from pygame import *
from pygame.sprite import *

IMG_URL = "./sprites/banana.png"

class Food(Sprite):
    def __init__(self, WIDTH, HEIGHT, SCALE=1):
        Sprite.__init__(self)
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCALE = SCALE
        self.img_scale = SCALE * 1.5
        picture = image.load(IMG_URL)
        picture = transform.scale(picture, (self.img_scale, self.img_scale)) # scale
        self.image = picture.convert_alpha()
        self.rect = None
        self.sprite = Group()
        self.change_position()
        self.sprite.add(self)
        
        
    def get_random_pos(self):
        # return (random.randrange(self.WIDTH), random.randrange(self.HEIGHT))
        new_pos = (random.randrange(self.WIDTH) * self.SCALE, random.randrange(self.HEIGHT) * self.SCALE)
        print(f"new food: {new_pos}")
        return new_pos
    
        
    def change_position(self):
        random_pos = self.get_random_pos()
        self.rect = Rect(random_pos[0], random_pos[1], self.img_scale, self.img_scale)
        


        