from card import Card


class Deck:
    def __init__(self, size=1):
        self._size = size
        self._ordered_deck = []

    def fill_deck(self):
        for suits in range(4):
            suit = "None"
            if suits == 0:
                suit = "Spades"
            if suits == 1:
                suit = "Clubs"
            if suits == 2:
                suit = "Diamonds"
            if suits == 3:
                suit = "Hearts"

            for number in range(1, 14):
                self._ordered_deck.append(Card(number, suit))

    def shuffle(self):
        pass

    def draw(self):
        return self._ordered_deck[0]

    def print_deck(self):
        for cards in self._ordered_deck:
            print(cards.print_card())


