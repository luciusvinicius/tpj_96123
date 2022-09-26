from player import Player

class Croupier(Player):
    def __init__(self, name, deck):
        super().__init__(name)
        self.deck = deck
    
    def give_card(self, player):
        player.add(self.deck.draw())