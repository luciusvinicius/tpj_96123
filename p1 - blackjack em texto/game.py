from croupier import Croupier
from deck import Deck
from deck import Deck
from player import Player

class Game:
    def __init__(self):
        croupier_name = input("Please insert Croupier name: ")
        self.croupier = Croupier(croupier_name, Deck(40))
        self.players = [self.croupier]
        i = 1
        while True:
            player_name = input(f"Please insert player {i}'s name: ")
            player = Player(player_name)
            self.players.append(player)
            add_player = input("Add another player? (y/n): ")
            if add_player.lower() != "y":
                break
            i += 1

        self._current_player = None

    def show_status(self):
        print("----Status----")
        print(*self.players, sep='\n')
        
    def play(self):
        i = 1
        num_finishes = 0
        while True:
            self.show_status()
            self._current_player = self.players[i%len(self.players)]

            if not self._current_player.has_finished:
                should_continue = input(f"{self._current_player.name}, draw one more? (y/n): ")
                if should_continue.lower() == "y":
                    self.croupier.give_card(self._current_player)
                else:
                    self._current_player.finish()
                    num_finishes += 1

            if num_finishes >= len(self.players):
                break

            i += 1