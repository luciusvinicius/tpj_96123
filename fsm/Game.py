from pygame import *

from Ant import Ant
from Food import Food
from House import House
from Spawner import Spawner
from Water import Water


class Game:
    def __init__(self, width, height, scale, fps, ttl, food_spawn_cooldown, water_spawn_cooldown):
        self.is_running = True
        self.width = width
        self.height = height
        self.scale = scale
        self.fps = fps
        self.ttl = ttl
        self.clock = time.Clock()
        self.screen = display.set_mode((self.width * self.scale, self.height * self.scale))

        self.home = House(self.width / 2, self.height / 2, scale, self.screen,
                          width=self.width, height=self.height)
        self.food_spawner = Spawner(Food, food_spawn_cooldown, scale, self.screen)
        self.water_spawner = Spawner(Water, water_spawn_cooldown, scale, self.screen)

        self.ants = [Ant(self.width / 2, self.height / 2, scale, self.screen,
                         ttl=ttl, width=self.width, height=self.height,
                         spawners=[self.food_spawner, self.water_spawner])]

        self.background_color = "gray"

    def run(self):
        while self.is_running:
            for e in event.get():
                if e.type == QUIT:
                    self.is_running = False

            self.screen.fill(self.background_color)

            for ant in self.ants:
                ant.update()

            self.food_spawner.update()
            self.water_spawner.update()
            self.home.update()
            display.flip()
            self.clock.tick(self.fps)
