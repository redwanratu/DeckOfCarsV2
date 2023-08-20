
class Card:
    """ Card Class """

    def __init__(self,value,suit):
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
        pass

    @suit.setter
    def suit(self,suit):
        self._suit=suit



    def __str__(self) -> str:
        return "[{}  {}]".format(self._value,self._suit)
    
    def show(self):
        print("[{}  {}]".format(self._value,self._suit))