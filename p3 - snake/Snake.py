from pygame import *
from pygame.sprite import *
import pygame

from Command import Down, Left, Right, Up
from BodyPart import BodyPart
from EventHandler import EventHandler
from Food import Food

BASE_DIR = "./sprites"

COMMANDS_LIST = [
    {
        pygame.K_w: Up,
        pygame.K_a: Left,
        pygame.K_s: Down,
        pygame.K_d: Right,
    },
    {
        pygame.K_UP: Up,
        pygame.K_LEFT: Left,
        pygame.K_DOWN: Down,
        pygame.K_RIGHT: Right,
    },
    {
        pygame.K_i: Up,
        pygame.K_j: Left,
        pygame.K_k: Down,
        pygame.K_l: Right,
    }
]

class Snake(Sprite):
    counter = 1
    def __init__(self, x, y, scale=0, length = 3, speed=1, direction = (1, 0), color="green", eventHandler=EventHandler()):
        self.length = 1
        self.root = BodyPart(x, y, direction, scale=scale, speed=speed)
        self.speed = speed
        self.last = self.root
        self.direction = direction
        
        if self.__class__.counter <= len(COMMANDS_LIST):
            self.commands = COMMANDS_LIST[self.__class__.counter - 1]
        else:
            self.commands = {}
        
        for command in self.commands:
            self.commands[command] = self.commands[command](self)
            
        self.event_handler = eventHandler
        self.event_handler.registry(self)
        self.id = self.__class__.counter
        self.__class__.counter += 1
        self.all_sprites = Group()
        self.all_sprites.add(self.root)
        self.scale = scale
        
        
        self.head_sprite = image.load(f"{BASE_DIR}/head-{color}.png")
        self.straight_sprite = image.load(f"{BASE_DIR}/straight-{color}.png")
        self.end_sprite = image.load(f"{BASE_DIR}/end-{color}.png")
        self.curve_sprite = image.load(f"{BASE_DIR}/curve-{color}.png")
        
        for _ in range(1, length):
            self.add_part()
                    
    def add_part(self):
        print(f"Added Part, Length = {self.length}")
        bp = BodyPart(self.last.rect.x - self.last.rect.width * self.last.direction[0], self.last.rect.y - self.last.direction[1] * self.last.rect.height, self.last.direction, scale=self.scale, speed=self.speed)
        
        bp.prev = self.last
        self.last.next = bp
        self.last = bp
        self.length += 1
        self.all_sprites.add(bp)
        
        
    def move(self, direction, width, height):
        body_part = self.last
        
        while True:
            prev = body_part.prev
        
            if prev is None:
                break

            body_part.move(prev.direction, width, height, self.scale)
            
            body_part.direction = prev.direction
            body_part = body_part.prev
        
        body_part.direction = direction
        body_part.move(direction, width, height, self.scale)
        
    def collides_with(self, fruit : Food):
        bd = self.root
        while True:
            if bd.rect.colliderect(fruit.rect):
                return True
            
            bd = bd.next
            
            if bd is None:
                return False
            
    def kills_itself(self):
        bp = self.root
        lst = [(bp.rect.x, bp.rect.y)]
        while True:
            nxt = bp.next
            if nxt is None:
                return False
            if (nxt.rect.x, nxt.rect.y) in lst:
                return True
            lst.append((nxt.rect.x, nxt.rect.y))
            bp = nxt
        
    def kills(self, snake):
        pass
    
    def crashes_into_wall(self, width, height):         
        return self.root.clashes_with_wall(width, height, self.scale)       
    
    def get_body_part_list(self):
        lst = []
        bp = self.root
        while True:
            lst.append(bp)
            
            if bp.next is None:
                return lst
            
            bp = bp.next
            

    def apply_scale(self):
        bp = self.last
        while True:
            bp.apply_scale(self.head_sprite, self.straight_sprite, self.end_sprite, self.curve_sprite)
            prev = bp.prev
            if prev is None:
                break
            bp = prev

    
    def set_head(self, body_part : BodyPart):
        body_part.set_sprite(self.head_sprite)
    
    def set_straight(self, body_part : BodyPart):
        body_part.set_sprite(self.straight_sprite)
    
    def set_end(self, body_part : BodyPart):
        body_part.set_sprite(self.end_sprite)
    
    def set_curve(self, body_part : BodyPart):        
        body_part.set_sprite(self.curve_sprite)
        
    def listen(self, event, args):
        if event.strip() == "snake_eat" and args[0] == self.id:
            self.add_part()
    
    
    def __str__(self):
        return f"Snake {self.id}"
            
        
            
    
            
        
        
        