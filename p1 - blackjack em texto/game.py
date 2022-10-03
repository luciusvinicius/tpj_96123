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
        while True:
            if not any(player.can_play() for player in self.players):
                break
            
            self.show_status()
            self._current_player = self.players[i%len(self.players)]

            if self._current_player.can_play():
                should_continue = self._current_player.play()
                if should_continue.lower() == "y":
                    self.croupier.give_card(self._current_player)
                else:
                    self._current_player.finish()

            i += 1
        self.finish_game()
        
    def finish_game(self):
        print("GAME ENDED")
        self.show_status()
        
        winner = None
        for player in self.players:
            if winner is None or player.get_final_score() > winner.get_final_score():
                winner = player
                
        print("And the winner is...")
        print(winner.name)