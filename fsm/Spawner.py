from Resource import Resource
from fsm import State, Transition, FSM


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
        wait = Wait()
        spawn = Spawn()
        states = [wait, spawn]
        transitions = {
            "spawn": Transition(wait, spawn),
            "update": Transition(spawn, wait)
        }
        self.fsm = FSM(states, transitions)

    def update(self):
        self.fsm.update("update", self)
        # self.timer += 1
        # if self.timer >= self.cooldown:
        #     self.entities.append(self.base_obj(self.scale, self.screen, self.width, self.height))
        #     self.timer = 0
        # for entity in self.entities:
        #     entity.update()


class Wait(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, obj: Spawner):
        obj.timer += 1
        if obj.timer >= obj.cooldown:
            obj.fsm.update("spawn", obj)
        for entity in obj.entities:
            entity.update()
        return super().update(obj)


class Spawn(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, obj: Spawner):
        obj.entities.append(obj.base_obj(obj.scale, obj.screen, obj.width, obj.height))
        obj.timer = 0
        return super().update(obj)
