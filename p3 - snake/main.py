from pygame import *
from pygame.sprite import *
import pygame
import random
from EventHandler import EventHandler
from EventHandlerSingleton import EventHandlerSingleton

from Food import Food

from Snake import Snake

WIDTH, HEIGHT = 80, 40
SCALE = 15
SPEED = 1
NUM_PLAYERS = 2
if NUM_PLAYERS < 1:
    NUM_PLAYERS = 1
    
COLORS = ["green", "yellow"]

display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()
event_handler = EventHandlerSingleton()
LENGTH = 3

handler = event_handler.get()
snakes = [Snake((i+1)*80, (i+1)*40, SCALE, LENGTH, SPEED, color=COLORS[i%len(COLORS)]) for i in range(NUM_PLAYERS)]

food = Food(WIDTH, HEIGHT, SCALE)
GAME_EVENT = pygame.event.custom_type()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            for snake in snakes:
                if event.key in snake.commands:
                    snake.commands[event.key].execute()
        elif event.type == GAME_EVENT:
            print(event.txt)
            
    display.fill("black")
    
    for snake in snakes:
        
        snake.all_sprites.draw(display)
        food.sprite.draw(display)

        body_part = snake.root

        if snake.collides_with(food):
            handler.notify("snake_eat", snake.id)
        
        # if snake.crashes_into_wall(WIDTH, HEIGHT):
        #     print("Snake crashed against the wall")
        #     running = False

        # if snake.kills_itself():
        #     print("Snake eats self")
        #     running = False
        
        # for snake2 in snakes:
        #     if snake2.id == snake.id: continue
        #     if snake.kills(snake2):
        #         print(f"{snake2} just got rect.")
        
        snake.move(snake.direction, WIDTH, HEIGHT)
        snake.apply_scale()
        
    pygame.display.flip()
    clock.tick(15)

pygame.quit()
