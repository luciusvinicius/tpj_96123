import random

VALUES = ['A',2,3,4,5,6,7,8,9,10,'D','J','K']

class Card:
    def __init__(self) -> None:
        self.value = random.choice(VALUES)
        
    def __repr__(self) -> str:
        return str(self.value)

