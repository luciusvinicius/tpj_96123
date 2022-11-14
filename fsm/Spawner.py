

class Spawner:
    def __init__(self, Obj, cooldown, scale, screen, width=80, height=60):
        self.base_obj = Obj
        self.entities = [Obj(scale, screen, width, height)]
        self.cooldown = cooldown
        self.timer = 0
        self.scale = scale
        self.screen = screen
        self.width = width
        self.height = height

    def update(self):
        self.timer += 1
        if self.timer >= self.cooldown:
            self.entities.append(self.base_obj(self.scale, self.screen, self.width, self.height))
            self.timer = 0
        for entity in self.entities:
            entity.update()

