from calendar import c
from card import Card

class Deck:
    def __init__(self, n_cards):
        self.cards = [Card() for _ in range(n_cards)]
        
    def __str__(self):
        return str(self.cards)
    
    def draw(self):
        return self.cards.pop()

    def get_score(self):
        totals = [0]
        for card in self.cards:
            # 'A' card all options
            if card.value == "A":
                totals *= 2
                
                for count in range(len(totals)):
                    if count < len(totals)/2:
                        totals[count] += 1
                    else:
                        totals[count] += 11
                continue
            
            for count in range(len(totals)):
                totals[count] += card.get_value()
            
        return totals

    
    def add(self, card):
        self.cards.append(card)