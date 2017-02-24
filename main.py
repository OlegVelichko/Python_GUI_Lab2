import random


class Card(object):

    ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    suite = 'Diamonds Hearts Spades Clubs'.split()

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Deck(object):

    def __init__(self):
        self.cards = [Card(r, s) for r in Card.ranks for s in Card.suite]

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        card = ''
        for i in self.cards:
            card = card + str(i.rank) + ' ' + str(i.suit) + '\n'
        return card


if __name__ == "__main__":

    deck = Deck()

    deck.shuffle()

    print(deck)
