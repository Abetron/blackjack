from deck import Deck
from card import Card


if __name__ == '__main__':
    deck = Deck(8)
    deck.fill_deck()
    deck.print_deck()

    card = Card(4, "Spades")