import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.suit + self.value


class Shoe:
    def __init__(self, num_deck=1):
        self.cards = num_deck * [Card(s, v)
                                 for s in ['♠', '♥', '♦', '♣']
                                 for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def __str__(self):
        tmp = ''
        for c in self.cards:
            # print(c.value)
            tmp += c.suit
            tmp += c.value
        return tmp
