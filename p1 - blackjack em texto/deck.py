from card import Card

class Deck:
    def __init__(self, n_cards):
        self.cards = [Card() for _ in range(n_cards)]
        
    def __str__(self):
        return str(self.cards)
    
    def draw(self):
        return self.cards.pop()

    def get_score(self):
        return sum(card.value for card in self.cards)
    
    def add(self, card):
        self.cards.append(card)