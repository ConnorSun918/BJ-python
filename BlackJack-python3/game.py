import math
import card
from hand import Hand


class Game:
    def __init__(self, shoe_num, deck_num, player_num, stand_soft17, strategy, strategy_df, historyWriter, infoWriter,
                 shoeCount):
        self.shoe_num = shoe_num
        self.deck_num = deck_num
        self.player_num = player_num
        self.stand_soft17 = stand_soft17
        self.strategy = strategy
        self.strategy_df = strategy_df
        self.historyWriter = historyWriter
        self.infoWriter = infoWriter
        self.shoeCount = shoeCount

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

        self.dealer = Hand()
        self.players = [Hand() for c in range(self.player_num)]
        self.players_status = [[] for c in range(self.player_num)]
        self.shoe = card.Shoe(self.shoe_num)
        self.i = 0

        self.play()

    def find_strategy(self, player_hand, dealer_top_hand):
        player_hand_and_index = self.data_frame.to_dict().get('Player Hand')
        reversed_dict = dict(map(reversed, player_hand_and_index.items()))
        index = reversed_dict.get(player_hand)
        return self.data_frame[dealer_top_hand][index]

    def play(self):
        self.shoe.shuffle()
        self.shoe.shuffle()
        self.shoe.shuffle()
        print('shoe' + str(self.shoeCount) + ': ' + self.shoe.__str__())

        # write shoe info in the info file
        self.infoWriter.write('shoe' + str(self.shoeCount) + ': ' + self.shoe.__str__())
        self.infoWriter.write('\n')
        roundCount = 1

        while self.i < self.shoe_num * 52 - 20:
            self.historyWriter.write(str(self.shoeCount) + ',')
            self.historyWriter.write(str(roundCount) + ',')
            self.deal_2_cards()
            self.dealer.get_value()

            for player in self.players:
                player.get_value()

            if self.dealer.value != 21:
                for player in self.players:
                    self.hit_to_hard_17(player)
                self.hit_to_hard_17(self.dealer)

            if self.i == self.shoe_num * 52 and self.dealer.value < 18:
                self.historyWriter.write('run out of card\n')
            else:
                self.write_history()

            self.write_count()
            roundCount += 1
            self.reset_new_around()

    def reset_new_around(self):
        self.dealer.clear_hand()
        for player in self.players:
            player.clear_hand()

    def write_history(self):
        # write dealer hand and value
        self.historyWriter.write(self.dealer.__str__() + ',' + self.dealer.value.__str__() + ','
                                 + self.dealer.hand[0].value + ',')

        # ------------------
        # write players hand, value and status
        # ------------------
        if self.dealer.value > 21:
            for player in self.players:
                self.historyWriter.write(player.__str__() + ',' + player.value.__str__() + ',')
                if player.value < 22:
                    self.historyWriter.write('W,')
                else:
                    self.historyWriter.write('L,')
                ##################
                # need to be fixed
                ##################
                self.historyWriter.write(player.action + ',')
                # self.historyWriter(' ,')
        else:
            for player in self.players:
                self.historyWriter.write(player.__str__() + ',' + player.value.__str__() + ',')
                if player.value < 22:
                    if self.dealer.value > player.value:
                        self.historyWriter.write('L,')
                    elif self.dealer.value == player.value:
                        self.historyWriter.write('P,')
                    else:
                        self.historyWriter.write('W,')
                else:
                    self.historyWriter.write('L,')
                ##################
                # need to be fixed
                ##################
                self.historyWriter.write(player.action + ',')
                # self.historyWriter(' ,')

    def hit_to_hard_17(self, playerOrHealer):
        while playerOrHealer.value <= 17 and self.i < self.shoe_num * 52:
            if playerOrHealer.value == 17 and not (
                    playerOrHealer.hand[0].value == 'A' or playerOrHealer.hand[1].value == 'A'):
                break
            self.deal_a_card(playerOrHealer)
            playerOrHealer.get_value()

    ################################################
    # deal first 2 cards to dealer and each player #
    ################################################
    def deal_2_cards(self):
        for x in range(2):
            self.deal_a_card(self.dealer)
            for player in self.players:
                self.deal_a_card(player)

    ###################################
    # deal 1 card to player or dealer #
    ###################################
    def deal_a_card(self, playerOrHealer):
        playerOrHealer.hand.append(self.shoe.cards[self.i])
        self.count_card()
        self.i += 1

    def count_card(self):
        cardValueStr = self.shoe.cards[self.i].value
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

    def write_count(self):
        remain_deck = math.ceil((len(self.shoe.cards) - self.i) / 52)
        if remain_deck != 0:
            self.HiLoTrue = self.HiLo // remain_deck
            self.HiOptITrue = self.HiOptI // remain_deck
            self.HiOptIITrue = self.HiOptII // remain_deck
            self.KOTrue = self.KO // remain_deck
            self.OmegaIITrue = self.OmegaII // remain_deck
            self.HalvesTrue = self.Halves // remain_deck
            self.ZenCountTrue = self.Halves // remain_deck
        else:
            self.HiLoTrue = self.HiLo
            self.HiOptITrue = self.HiOptI
            self.HiOptIITrue = self.HiOptII
            self.KOTrue = self.KO
            self.OmegaIITrue = self.OmegaII
            self.HalvesTrue = self.Halves
            self.ZenCountTrue = self.Halves

        # write count and remaining cards in shoe in history file
        self.historyWriter.write(self.HiLo.__str__() + ',' + self.HiLoTrue.__str__() + ','
                                 + self.HiOptI.__str__() + ',' + self.HiOptITrue.__str__() + ','
                                 + self.HiOptII.__str__() + ',' + self.HiOptIITrue.__str__() + ','
                                 + self.KO.__str__() + ',' + self.KOTrue.__str__() + ','
                                 + self.OmegaII.__str__() + ',' + self.OmegaIITrue.__str__() + ','
                                 + self.Halves.__str__() + ',' + self.HalvesTrue.__str__() + ','
                                 + self.ZenCount.__str__() + ',' + self.ZenCountTrue.__str__() + ','
                                 + (len(self.shoe.cards) - self.i).__str__() + ', \n')
