from deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Deck(3)
        self.has_finished = False
        
    def __str__(self):
        return f"{self.name}: {self.hand}"

    def add(self, card):
        self.hand.add(card)

    def get_score(self):
        return self.hand.get_score()

    def finish(self):
        self.has_finished = True