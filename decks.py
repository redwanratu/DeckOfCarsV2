from abstract import Deck
from card import Card

class SimpleDeck(Deck):
    """ Concrete Deck Class """
    
    def __init__(self) -> None:
        self.cards=[]
        self._create_deck()

    def __str__(self) -> str:
        return "A Deck of {} cards".format(len(self.cards))
    
    def _create_deck(self):
        suits=["Spade","Diamond","Club","Heart"]
        values=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        for suit in suits:
            for value in values:  
                card=Card(value,suit)
                self.cards.append(card)
            
    def show(self):
        for card in self.cards:
            card.show()
    
    @property
    def deck(self):
        return self.cards