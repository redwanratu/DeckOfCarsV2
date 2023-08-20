from abstract import Display
from trick import Trick
from utils import gap
import os

class PlayerDisplay(Display):
    def __init__(self):
        self.trick = None
        self.messages = []
        self.player = int()

    def display(self,*args, **kwrgs):
        os.system('clear')

        self.display_scoreboard()
        
        if self.trick: 
            self.trick.display_trick_state()
        
        self.display_cards(*args, **kwrgs)
        
        self.display_message()


    def set_trick(self, trick: Trick):
        self.trick = trick
        

    def set_cards_on_board(self):
        return super().set_cards_on_board()
    
    def set_cards_on_hand():
        pass

    def display_scoreboard(self):
        print("SCORECARD: ")
        if self.trick:
            # for trick in self.trick:
            self.trick.display_winner()
        gap(1)
    
    def game_winner(self):
        max_win=max(self.score)
        return self.score.index(max_win) +1
    
    def display_cards(self, player, cards : list):
        print(f"Player {player+1} Cards: \n")
        hand= "\t".join(f"{card}" for card in cards)
        serial="\t\t".join(f"{i}" for i in range(1,len(cards)+1))
        print(f"{hand}\n{serial}")

        gap(4)

    def display_message(self):
        if self.messages:
            for message in self.messages:
                print(message)


    def set_massage(self, message: list | str):
        if type(message) is str:
            message = [message]
        self.messages.extend(message)