from typing import Tuple, overload
from pygame import *
from pygame.sprite import *
import math

IMG_URL = "./sprites/banana.jpg"

angles = {
    (0,1): {
        (1,0): 180,
        (-1,0): -90
    },
    (0,-1): {
        (1,0): 90,
        (-1,0): 0
    },
    (1,0): {
        (0,1): 0,
        (0,-1): -90
    },
    (-1,0): {
        (0,1): 90,
        (0,-1): 180
    }
}


class BodyPart(Sprite):
    counter = 1
    def __init__(self, x, y, direction, scale=1, speed=1):
        Sprite.__init__(self)
        print("init body part")
        # self.x : int = x-35
        # self.y : int = y-18
        
        self.x : int = x
        self.y : int = y
        self.speed = speed
        self.img_scale = scale * 1.5
        self.id = self.__class__.counter
        self.__class__.counter += 1

        self.rect = Rect(self.x, self.y, self.img_scale, self.img_scale)
        self.prev : BodyPart = None
        self.next : BodyPart = None
        self.direction : Tuple = direction
        self.angle : int = 0
        # self.scale = scale
        self.previous_direction : Tuple = direction

        picture = image.load(IMG_URL)
        picture = transform.scale(picture, (self.img_scale, self.img_scale)) # scale
        self.base_image = picture.convert_alpha()
        self.image = picture.convert_alpha()
        self.type = "end"

    def move(self, direction):
        self.rect.move_ip((direction[0] * self.rect.width * self.speed, direction[1] * self.rect.height * self.speed))
        # print(self.rect)
        # print(self.scale)
        self.x += direction[0]*self.speed
        self.y += direction[1]*self.speed

    def apply_scale(self, head_sprite, straight_sprite, end_sprite, curve_sprite):
        self.image = transform.scale(self.base_image, (self.img_scale, self.img_scale))
        
        angle = self.get_curve_angle()
        nxt = self.next
        prev = self.prev
        
        if angle is not None:
            print(f"{self}: {self.angle=}")
            self.set_sprite(curve_sprite)

        else:
            angle_x = 0 if self.direction[0] >= 0 else 180
            angle = - 90 * self.direction[1] + angle_x
            if nxt is None:
                self.set_sprite(end_sprite)
            elif prev is None:
                self.set_sprite(head_sprite)
            else:
                self.set_sprite(straight_sprite)
            
        self.image = transform.rotate(self.image, angle)


    def set_sprite(self, sprite):
        self.base_image = transform.scale(sprite, (self.img_scale, self.img_scale))
        picture = transform.scale(sprite, (self.img_scale, self.img_scale))
        self.get_curve_angle()
        self.image = picture.convert_alpha()

    def get_curve_angle(self):
        # print("-------------")
        prev = self.prev
        if prev is not None and prev.direction != self.direction:
            # print(f"{prev.direction=}")
            # print(f"{self.direction=}")
            # print(f"{angles[self.direction][prev.direction]}")
            self.angle = angles[self.direction][prev.direction]
            print(f"set {self} {self.angle=}")
            return self.angle
        
        return None

    def get_previously_angle(self):
        prev = self.prev
        if prev is not None and self.id == 2:
            print(f"{prev.direction=}")
            print(f"{self.direction=}")
        if prev is not None and prev.direction != self.previous_direction:
            # print(f"{prev.direction=}")
            # print(f"{self.direction=}")
            # print(f"{angles[self.direction][prev.direction]}")
            self.angle = angles[self.previous_direction][prev.direction]
            print(f"set {self} {self.angle=}")
            return self.angle
        
        return None

    def set_direction(self, direction):
        self.previous_direction = self.direction
        self.direction = direction


    def __str__(self):
        return f"BodyPart {self.id}: ({self.rect.x}, {self.rect.y})"


    # @move.overload
    # def move(self, x, y):
    #     self.rect.move_ip(x, y)