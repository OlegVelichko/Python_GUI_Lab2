import random

def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


class Card(object):

    ranks = None
    suite = None

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


@singleton
class Deck(object):

    ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    suite = 'Diamonds Hearts Spades Clubs'.split()

    def __init__(self):
        self.cards = [Card(r, s) for r in self.ranks for s in self.suite]

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
