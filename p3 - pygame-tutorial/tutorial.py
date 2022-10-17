from pygame import *
import pygame
from pygame.font import Font
from pygame.sprite import *
from pygame.mixer import *
from BulletBill import BulletBill
from SussyCosta import SussyCosta

pygame.init()
mixer.init()

screen = display.set_mode((1200, 800))
display.set_caption("Super Sussy Costa World")

text = Font("./fonts/Qdbettercomicsans-jEEeG.ttf", 24)

all_sprites = Group()
cc = SussyCosta(500, 300)
bb = BulletBill(200, 200)
all_sprites.add(cc)
all_sprites.add(bb)

music.load("./sounds/Among us Drip Theme song - Trap Remix.mp3")
music.play(loops=-1)

MOVEMENT_SPEED = 10
FPS = 60

def handle_input(key):
    undo = (0, 0)
    
    if key[K_UP]:
        undo = (0, MOVEMENT_SPEED)
        cc.move((0, -MOVEMENT_SPEED))
    if key[K_DOWN]:
        undo = (0, -MOVEMENT_SPEED)
        cc.move((0, MOVEMENT_SPEED))
    if key[K_LEFT]:
        undo = (MOVEMENT_SPEED, 0)
        cc.move((-MOVEMENT_SPEED, 0))
    if key[K_RIGHT]:
        undo = (-MOVEMENT_SPEED, 0)
        cc.move((MOVEMENT_SPEED, 0))
        
    if cc.rect.colliderect(bb.rect):
        cc.move(undo)

clock = time.Clock()
while True:
    keys = pygame.key.get_pressed()
    handle_input(keys)
    
    for e in event.get():
        if e.type == QUIT:
            pygame.quit()
            break

    
    text_surface = text.render("Amogus", True, (0, 0, 0))
    

    screen.fill((10, 100, 100))
    all_sprites.draw(screen)
    # pygame.Surface.blit(screen, text_surface)
    clock.tick(FPS)
    display.update()