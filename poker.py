class card:
    def _init_(self, ):
        SUITS = ("" , "", "")
        RANKS = ("2", "3", "4", "5","6", "7", "8", "9", "10", "J", "Q", "K", "A")
    def _int_(self, rank, suit):
        if rank not in self RANKS:
            raise Exception(f"Invalid rank, must be one of (self.RANKS)")
        if suit is not in self SUITS:
            raise Exception(f"Invalid suit, must be one of (self.RANKS)")
        self._rank = rank
        self._suit = suit
     @property
    def suit(self):
        return self._rank
     def _str_(self):
         return f"(self.rank)(self.suit)"

    def _str_(self):
        return self._str_()

    c1 = Card ("A", "")
    #c2 = Card ("1", "")
    #c3 = Card ("7", "")
    print(c1)
    c2 = Card ("Q", "")
    print(c2)

Class Deck:
    def _init_(self):
        cards = ()
        # iterate over all ranks and suits, create a card and add it to the list
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                card = Card(rank, suit)
                cards.append
            self._cards = cards