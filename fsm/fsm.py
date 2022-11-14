class State:
    def __init__(self, name) -> None:
        self.name = name

    def enter(self):
        print(f"Entering {self.name}")

    def update(self, obj):
        pass

    def exit(self):
        pass


class Transition:
    def __init__(self, _from, _to) -> None:
        self._from = _from
        self._to = _to


class Idle(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, obj):
        print("waiting for your command...")
        return super().update(obj)


class Walk(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, obj):
        print("Moving")
        return super().update(obj)


class FSM:
    def __init__(self, states: list[State], transitions: dict[Transition]) -> None:
        self._states = states
        self._transitions = transitions

        self.current: State = self._states[0]
        self.end: State = self._states[-1]

    def update(self, event, object):
        if event:
            trans = self._transitions.get(event)
            if trans and trans._from == self.current:
                self.current.exit()
                self.current = trans._to
                self.current.enter()
        self.current.update(object)

        if self.current == self.end:
            self.current.exit()
            return False
        return True


if __name__ == "__main__":
    walk = Walk()
    idle = Idle()
    dead = State("Dead")

    states = [walk, idle, dead]
    transitions = {
        "rest": Transition(walk, idle),
        "engage": Transition(idle, walk),
        "harakiri": Transition(idle, dead)
    }

    fsm = FSM(states, transitions)

    event = None
    while fsm.update(event, None):
        event = input(">")
