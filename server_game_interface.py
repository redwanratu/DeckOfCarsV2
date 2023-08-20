from abstract import Game
from typing import List
from players import Player
from dealer import Dealer
from trick import Trick
from card import Card

class ServerGame(Game):
    def __init__(self, dealer: Dealer) -> None:
        self.players = []
        self.dealed_cards = dealer.getCards()
        self.tricks: List[Trick] = []
        self.player_to_play = 0

    def set_players(self, player: Player) -> None:
        self.players.append(player)

    def get_card_on_hands(self,player: Player, * args, **kwargs) -> List[Card]:
        player_id = self.get_player_id(player)
        return self.dealed_cards[player_id].get_hand_cards()
    
    def get_card_on_boards(self) -> List[Card]:
        if self.tricks:
            return self.tricks[-1].cards
        return []

    def play(self, *args, **kwargs) -> bool:
        if not self.tricks:
            trick = self.get_new_trick()
            self.tricks.append(trick)

        trick = self.tricks[-1]

        if trick.get_basesuit() and kwargs.get("card").suit != trick.get_basesuit() and trick.get_basesuit() in [card.suit for card in self.get_card_on_hands(**kwargs)]:
            return False

        trick.play(*args, **kwargs)
        
        if len(trick.cards) == 4:
            card, winner_player = trick.get_winner()
            trick = self.get_new_trick()
            self.tricks.append(trick)
            self.set_next_player_to_play(winner_player)
        else:
            self.set_next_player_to_play()

        self.get_card_on_hands(**kwargs).remove(kwargs.get("card"))
        return True

    def get_player_id(self, player: Player) -> int:
        for i in range(len(self.players)):
            if self.players[i].username == player.username:
                return i

    def get_player_to_play(self) -> Player:
        return self.players[self.player_to_play]

    def get_new_trick(self):
        return Trick()
    
    def has_turn(self, player: Player) -> bool:
        if self.get_player_id(player=player) == self.player_to_play:
            return True
        
    def set_next_player_to_play(self, winner_player: Player = None):
        if not winner_player:
            self.player_to_play = (self.player_to_play + 1) % 4
            return 
            
        self.player_to_play = self.get_player_id(winner_player) 







