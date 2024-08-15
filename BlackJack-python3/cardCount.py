class cardCount:
    def __init__(self):
        self.round_num = 0
        self.count = 0
        self.trueCount = 0
        self.HiLo = 0
        self.HiLoTrue = 0
        self.HiOptI = 0
        self.HiOptITrue = 0
        self.HiOptII = 0
        self.HiOptIITrue = 0
        self.KO = 0
        self.KOTrue = 0
        self.OmegaII = 0
        self.OmegaIITrue = 0
        self.Halves = 0
        self.HalvesTrue = 0
        self.ZenCount = 0
        self.ZenCountTrue = 0

    def count_card(self, cardValueStr):
        # cardValueStr = self.shoe.cards[self.i].value
        if cardValueStr == '2':
            self.HiLo += 1
            self.HiOptI = 0
            self.HiOptII += 1
            self.KO += 1
            self.OmegaII += 1
            self.Halves += .5
            self.ZenCount += 1
        elif cardValueStr == '3':
            self.HiLo += 1
            self.HiOptI = 1
            self.HiOptII += 1
            self.KO += 1
            self.OmegaII += 1
            self.Halves += 1
            self.ZenCount += 1
        elif cardValueStr == '4':
            self.HiLo += 1
            self.HiOptI = 1
            self.HiOptII += 2
            self.KO += 1
            self.OmegaII += 2
            self.Halves += 1
            self.ZenCount += 2
        elif cardValueStr == '5':
            self.HiLo += 1
            self.HiOptI = 1
            self.HiOptII += 2
            self.KO += 1
            self.OmegaII += 2
            self.Halves += 1.5
            self.ZenCount += 2
        elif cardValueStr == '6':
            self.HiLo += 1
            self.HiOptI = 1
            self.HiOptII += 1
            self.KO += 1
            self.OmegaII += 2
            self.Halves += 1
            self.ZenCount += 2
        elif cardValueStr == '7':
            self.HiLo += 0
            self.HiOptI = 0
            self.HiOptII += 1
            self.KO += 1
            self.OmegaII += 1
            self.Halves += .5
            self.ZenCount += 1
        elif cardValueStr == '8':
            self.HiLo += 0
            self.HiOptI = 0
            self.HiOptII += 0
            self.KO += 0
            self.OmegaII += 0
            self.Halves += 0
            self.ZenCount += 0
        elif cardValueStr == '9':
            self.HiLo += 0
            self.HiOptI = 0
            self.HiOptII += 0
            self.KO += 0
            self.OmegaII -= 1
            self.Halves += .5
            self.ZenCount += 0
        elif cardValueStr == '10' or cardValueStr == 'J' or cardValueStr == 'Q' or cardValueStr == 'K':
            self.HiLo -= 1
            self.HiOptI -= 1
            self.HiOptII -= 2
            self.KO -= 1
            self.OmegaII -= 2
            self.Halves -= 1
            self.ZenCount -= 2
        elif cardValueStr == 'A':
            self.HiLo -= 1
            self.HiOptI -= 0
            self.HiOptII -= 0
            self.KO -= 1
            self.OmegaII -= 0
            self.Halves -= 1
            self.ZenCount -= 1
        else:
            print('something went wrong during the counting')
            print('the card is: ' + cardValueStr)