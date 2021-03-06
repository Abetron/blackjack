from card import Card
from secrets import randbelow
from linkedList import LinkedList


class Deck:
    def __init__(self, num_of_decks=1):
        self._size = num_of_decks
        self._ordered_deck = []
        self._deck = LinkedList()

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
        deck_size = len(self._ordered_deck)

        while deck_size > 0:
            random_card = randbelow(deck_size)

            card = self._ordered_deck[random_card]

            self._deck.append(card)

            self.swap(self._ordered_deck, random_card, (deck_size - 1))
            deck_size -= 1

    def draw(self):
        current_head = self._deck.get_head()
        self._deck.set_head(current_head.get_next())
        return current_head.get_data()

    def print_deck(self):
        for cards in self._ordered_deck:
            print(cards.print_card())

    def swap(self, deck, a=int, b=int):
        placeholder = deck[a]
        deck[a] = deck[b]
        deck[b] = placeholder
