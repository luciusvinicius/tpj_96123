from deck import Deck

LIMIT = 21

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Deck(2)
        self.has_finished = False
        
    def __str__(self):
        res = f"{self.name}: {self.hand} - {self.hand.get_score()}"
        if self.has_busted():
            res += " - BUST"
        return res

    def add(self, card):
        self.hand.add(card)

    def get_score(self):
        return self.hand.get_score()
    
    def get_final_score(self):
        ma = 0
        for score in self.get_score():
            if score > ma and score <= LIMIT:
                ma = score
        return ma
    
    def has_busted(self):
        return min(self.get_score()) > 21
    
    def can_play(self):
        return not self.has_finished and not self.has_busted()
    def finish(self):
        self.has_finished = True