from pygame import *
from pygame.sprite import *
import pygame
import random
from Command import Down, Left, Right, Up
from Food import Food

from Snake import Snake

WIDTH, HEIGHT = 80, 40
SCALE = 10

display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()
LENGTH = 1
snake = Snake(40, 20, SCALE, LENGTH)
print(f"Snake root {snake.root}")
# snake_body = [(40, 20), (39, 20), (38, 20)]
# snake_direction = (1, 0)
# snake_length = 3
# food = (random.randrange(WIDTH), random.randrange(HEIGHT))
food = Food(WIDTH, HEIGHT)
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
            COMMANDS[event.key].execute()

        elif event.type == GAME_EVENT:
            print(event.txt)
            
            
    display.fill("black")
    snake.all_sprites.draw(display)
    food.sprite.draw(display)

    # pygame.draw.rect(display, "green", (SCALE * food[0], SCALE * food[1], SCALE, SCALE))
    body_part = snake.root
    while True:
        
        x = body_part.x
        y = body_part.y
        # pygame.draw.rect(display, "red", (SCALE * x, SCALE * y, SCALE, SCALE))

        if snake.collides_with(food):
            snake.add_part()
            food.change_position()

        if x not in range(WIDTH) or y not in range(HEIGHT):
            print("Snake crashed against the wall")
            running = False
            
        if body_part.next is None:
            break
        
        body_part = body_part.next

        if snake.kills_itself():
            print("Snake eats self")
            running = False

    # move snake
    # snake_body[0:0] = [
    #     (snake_body[0][0] + snake_direction[0], snake_body[0][1] + snake_direction[1])
    # ]
    
    snake.move(snake.direction)
    
    # while len(snake.body) > snake_length:
    #     snake_body.pop()

    # update window
    pygame.display.flip()
    clock.tick(15)

pygame.quit()
