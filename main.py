from deck import Deck
from card import Card


if __name__ == '__main__':
    deck = Deck(1)
    deck.fill_deck()
    deck.shuffle()
    card = deck.draw().get_data()

    for i in range(52):
        card = deck.draw().get_data()
        print(card.print_card())