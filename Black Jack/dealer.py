from suffles import RegularSuffle
from decks import SimpleDeck
class Dealer:
    def __init__(self,deck=SimpleDeck()) -> None:
        # create a instance of playing deck
        self.deck=deck
        self.suffled_deck=RegularSuffle(self.deck.deck)
        #self._suffle_deal()


    def _suffle_deal(self):
        #create  a instance of regular suffle deck
        pass


    def getCards(self):


        # # # #create  a instance of regular suffle deck
        # # # self.suffled_deck=RegularSuffle(self.deck.deck)

        # shuffle deal and show cards
        #self.suffled_deck=self.suffled_deck.suffle().deal().show().get_player_cards()
        self.suffled_deck=self.suffled_deck.suffle().deal().get_player_cards()
        
        return self.suffled_deck

    




        

         
    
