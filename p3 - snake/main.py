from pygame import *
from pygame.sprite import *
import pygame
import random
from Command import Down, Left, Right, Up
from Food import Food

from Snake import Snake

WIDTH, HEIGHT = 80, 40
SCALE = 10
SPEED = 1

display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()
LENGTH = 1
snake = Snake(40, 20, SCALE, LENGTH, SPEED)
print(f"Snake root {snake.root}")
# snake_body = [(40, 20), (39, 20), (38, 20)]
# snake_direction = (1, 0)
# snake_length = 3
# food = (random.randrange(WIDTH), random.randrange(HEIGHT))
food = Food(WIDTH, HEIGHT, SCALE)
GAME_EVENT = pygame.event.custom_type()


COMMANDS = {
    pygame.K_w: Up(snake),
    pygame.K_a: Left(snake),
    pygame.K_s: Down(snake),
    pygame.K_d: Right(snake),
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            try:
                COMMANDS[event.key].execute()
            except KeyError:
                pass

        elif event.type == GAME_EVENT:
            print(event.txt)
            
            
    display.fill("black")
    snake.all_sprites.draw(display)
    food.sprite.draw(display)

    body_part = snake.root

    if snake.collides_with(food):
        snake.add_part()
        food.change_position()
    
    if snake.crashes_into_wall(WIDTH, HEIGHT):
        print("Snake crashed against the wall")
        running = False

    if snake.kills_itself():
        print("Snake eats self")
        running = False
        
    snake.move(snake.direction)
    # update window
    snake.apply_scale()
    pygame.display.flip()
    clock.tick(15)

pygame.quit()