import random

LETTERS = {
    'D': 10,
    'J': 10,
    'K': 10
}

VALUES = ['A',2,3,4,5,6,7,8,9,10,'D','J','K']

class Card:
    def __init__(self):
        self.value = random.choice(VALUES)
        
    def __repr__(self):
        return str(self.value)
    
    def get_value(self):
        return self.value if isinstance(self.value, int) else LETTERS[self.value]
    
    

