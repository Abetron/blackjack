class Card:
    def __init__(self, number, suit: str):
        self._number = number
        self._suit = suit

    def get_number(self):
        return self._number

    def get_suit(self):
        return self._suit

    def print_card(self):
        rank = str(self._number)
        if self._number == 1:
            rank = "Ace"
        elif self._number == 11:
            rank = "Jack"
        elif self._number == 12:
            rank = "Queen"
        elif self._number == 13:
            rank = "King"

        return rank + " of " + self._suit
