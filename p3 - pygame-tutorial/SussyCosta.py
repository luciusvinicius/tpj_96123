from pygame import *
from pygame.sprite import *

from Object import Object

IMG_URL = "./monke-transparent.png"

class SussyCosta(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        
        picture = image.load(IMG_URL)
        picture = transform.scale(picture, (200, 200)) # scale
        self.image = picture.convert_alpha()
    