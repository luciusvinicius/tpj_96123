from player import Player

class Croupier(Player):
    def __init__(self, name, deck):
        super().__init__(name)
        self.deck = deck
    
    def give_card(self, player):
        player.add(self.deck.draw())
        
    def can_play(self):
        return super().can_play() and min(self.get_score()) < 17