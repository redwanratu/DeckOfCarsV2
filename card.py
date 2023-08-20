
class Card:
    """ Card Class """

    def __init__(self,value=None,suit=None):
        if suit != None:
            self._suit=suit
        else:
            self._suit=str(suit)
        self._value=value
    
    @property
    def value(self):
        pass

    @value.setter
    def value(self,value):
        self._value=value
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self,suit):
        self._suit=suit



    def __str__(self) -> str:
        return "[{}  {}]".format(self._value,self._suit)
    
    def show(self):
        print("[{}  {}]".format(self._value,self._suit))

    def card_face(self) -> dict:
        return {
            "suit": self._suit,
            "value": self._value
        }
