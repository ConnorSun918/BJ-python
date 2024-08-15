class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.action = ''

    def __str__(self):
        tmp = ''
        for c in self.hand:
            tmp += c.suit
            tmp += c.value
        return tmp

    def clear_hand(self):
        self.hand = []
        self.value = 0
        self.action = ''

    def get_value(self):
        self.value = 0
        A_Count = 0
        for card in self.hand:
            if card.value == '2':
                self.value += 2
            elif card.value == '3':
                self.value += 3
            elif card.value == '4':
                self.value += 4
            elif card.value == '5':
                self.value += 5
            elif card.value == '6':
                self.value += 6
            elif card.value == '7':
                self.value += 7
            elif card.value == '8':
                self.value += 8
            elif card.value == '9':
                self.value += 9
            elif card.value == '10':
                self.value += 10
            elif card.value == 'J':
                self.value += 10
            elif card.value == 'Q':
                self.value += 10
            elif card.value == 'K':
                self.value += 10
            elif card.value == 'A':
                A_Count += 1
                self.value += 11
            else:
                print("there's some thing went wrong with card value: ", card.value)
        if self.value > 21:
            for i in range(A_Count):
                if self.value < 21:
                    continue
                else:
                    self.value -= 10

        return self.value
