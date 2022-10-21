from pygame import *
from pygame.sprite import *
 
from BodyPart import BodyPart
from Food import Food

BASE_DIR = "./sprites"

class Snake(Sprite):
    def __init__(self, x, y, scale=0, length = 3, speed=1, direction = (1, 0), color="green"):
        self.length = 1
        self.root = BodyPart(x, y, direction, scale=scale, speed=speed)
        self.speed = speed
        self.last = self.root
        self.direction = direction
        self.all_sprites = Group()
        self.all_sprites.add(self.root)
        self.scale = scale
        
        self.head_sprite = image.load(f"{BASE_DIR}/head-{color}.png")
        self.straight_sprite = image.load(f"{BASE_DIR}/straight-{color}.png")
        self.end_sprite = image.load(f"{BASE_DIR}/end-{color}.png")
        self.curve_sprite = image.load(f"{BASE_DIR}/curve-{color}.png")
        
        self.set_head(self.root)
        
        for _ in range(1, length):
            self.add_part()
                    
    def add_part(self):
        print(f"Added Part, Length = {self.length}")
        bp = BodyPart(self.last.rect.x - self.last.rect.width * self.last.direction[0], self.last.rect.y - self.last.direction[1] * self.last.rect.height, self.last.direction, scale=self.scale, speed=self.speed)
        self.set_end(bp)
        # bp = BodyPart(self.last.rect.x - self.last.rect.width * self.last.direction[0], self.last.rect.y - self.last.direction[1] * self.last.rect.height, self.last.direction, self.scale)
        # bp = BodyPart(self.last.rect.x - self.last.direction[0] * self.scale, self.last.rect.y - self.last.direction[1] * self.scale, self.last.direction, self.scale)
        
        bp.prev = self.last
        self.last.next = bp
        self.last = bp
        self.length += 1
        self.all_sprites.add(bp)
        # self.body.append(bp)
        
    def move(self, direction):
        # self.root.move(direction)
        body_part = self.last
        
        while True:
            prev = body_part.prev
            
            if prev is None:
                break
            
            body_part.move(prev.direction)
            self.set_straight(body_part)
            body_part.direction = prev.direction
            body_part = body_part.prev
        
        body_part.direction = direction
        self.set_head(body_part)
        body_part.move(direction)
        
        
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
    
    def crashes_into_wall(self, WIDTH, HEIGHT):
        # bp = self.root
        # while True:
        #     if bp.x not in range(WIDTH) or bp.y not in range(HEIGHT):
        #         print("Snake crashed against the wall")
        #         return True
            
        #     nxt = bp.next
        #     if nxt is None:
                
        return self.root.rect.x not in range(WIDTH * self.scale) or self.root.rect.y not in range(HEIGHT * self.scale)

    def apply_scale(self):
        bp = self.root
        while True:
            bp.apply_scale(self.scale)
            nxt = bp.next
            if nxt is None:
                break
            bp = nxt

    
    def set_head(self, body_part : BodyPart):
        body_part.set_sprite(self.head_sprite)
    
    def set_straight(self, body_part : BodyPart):
        body_part.set_sprite(self.straight_sprite)
    
    def set_end(self, body_part : BodyPart):
        body_part.set_sprite(self.end_sprite)
    
    def set_curve(self, body_part : BodyPart):
        body_part.set_sprite(self.curve_sprite)
            
        
            
    
            
        
        
        