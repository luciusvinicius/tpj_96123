from Game import Game

WIDTH, HEIGHT = 40, 20
SCALE = 15
FPS = 24
TTL = 100
FOOD_SPAWN_COOLDOWN = 10


def main():
    game = Game(WIDTH, HEIGHT, SCALE, FPS, TTL, FOOD_SPAWN_COOLDOWN)
    game.run()


if __name__ == "__main__":
    main()
