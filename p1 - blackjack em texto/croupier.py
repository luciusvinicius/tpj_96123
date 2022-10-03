from player import Player

CROUPIER_LIMIT = 17

class Croupier(Player):
    def __init__(self, name, deck):
        super().__init__(name)
        self.deck = deck
    
    def give_card(self, player):
        player.add(self.deck.draw())
    
    def play(self):
        if super().get_final_score() < CROUPIER_LIMIT:
            return "y"
        return "n"
        
    def can_play(self):
        return super().can_play() and min(self.get_score()) < 17