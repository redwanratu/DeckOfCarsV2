from abstract import Suffle
from typing import List
from card import Card
import random

class CardOnHands:
    def __init__(self) -> None:
        self.cards = []
    
    def take_card_from_dealed_card(self, card: Card) -> None:
        self.cards.append(card)
    
    def get_hand_cards(self):
        return self.cards

    def has_basesuit(self, suit: str):
        for card in self.cards:
            if card.suit == suit:
                return True


class RegularSuffle(Suffle):
    def __init__(self, deck=None):
        super().__init__(deck)
        self.deal_deck=[]
        
    
    def suffle(self):
        self.deck=random.sample(self.deck,len(self.deck))
        return self
        

    def show(self):
        i=1
        for player_deck in self.deal_deck:
            print(f"******  Player {i}   ********")
            for card in player_deck:
                card.show()
            i+=1
        return self
            
    def deal(self,no_of_player=4,card_per_deal=1):
        if len(self.deck) % no_of_player != 0:
            raise ValueError(" Can,t equally distributed")
        
        # player_deck=[]
        for player in range(no_of_player):
            player_deck = CardOnHands()
            for i in range(player,len(self.deck),no_of_player):
                player_deck.take_card_from_dealed_card(self.deck[i])
            self.deal_deck.append(player_deck)
            
        return self
    
    def get_player_cards(self) -> List[Card]:
        return self.deal_deck


        
