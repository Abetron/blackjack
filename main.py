from deck import Deck


if __name__ == '__main__':
    deck = Deck(1)
    deck.fill_deck()
    deck.shuffle()

    for i in range(52):
        card = deck.draw()
        print(card.print_card())
