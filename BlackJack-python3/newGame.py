import math

import card
from cardCount import cardCount
from hand import Hand


class newGame:
    def __init__(self, parameterObj, shoeCount):
        self.parameterObj = parameterObj
        # self.cardCountObj = cardCountObj
        self.cardCountObj = cardCount()
        self.shoeCount = shoeCount
        self.cardCount = cardCount()
        self.dealer = Hand()
        self.players = [Hand() for c in range(self.parameterObj.player_num)]
        self.players_status = [[] for c in range(self.parameterObj.player_num)]
        self.shoe = card.Shoe(self.parameterObj.shoe_num)
        self.i = 0

        self.play()

    def play(self):
        self.shoe.shuffle()
        self.shoe.shuffle()
        self.shoe.shuffle()
        print('shoe' + str(self.shoeCount) + ': ' + self.shoe.__str__())

        # write shoe info in the info file
        self.parameterObj.infoWriter.write('shoe' + str(self.shoeCount) + ': ' + self.shoe.__str__())
        self.parameterObj.infoWriter.write('\n')
        roundCount = 1

        while self.i < self.parameterObj.shoe_num * 52 - 20:
            self.parameterObj.historyWriter.write(str(self.shoeCount) + ',')
            self.parameterObj.historyWriter.write(str(roundCount) + ',')
            self.deal_2_cards()
            self.dealer.get_value()

            for player in self.players:
                player.get_value()

            # if dealer doesn't have bj
            if self.dealer.value != 21:
                for player in self.players:
                    actionStr = self.parameterObj.find_strategy(player, self.dealer)
                    print(actionStr)
                    # self.hit_to_hard_17(player)
                self.hit_to_hard_17(self.dealer)

            if self.i == self.parameterObj.shoe_num * 52 and self.dealer.value < 18:
                self.parameterObj.historyWriter.write('run out of card\n')
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
        self.parameterObj.historyWriter.write(self.dealer.__str__() + ',' + self.dealer.value.__str__() + ','
                                              + self.dealer.hand[0].value + ',')

        # ------------------
        # write players hand, value and status
        # ------------------
        if self.dealer.value > 21:
            for player in self.players:
                self.parameterObj.historyWriter.write(player.__str__() + ',' + player.value.__str__() + ',')
                if player.value < 22:
                    self.parameterObj.historyWriter.write('W,')
                else:
                    self.parameterObj.historyWriter.write('L,')
                ##################
                # need to be fixed
                ##################
                self.parameterObj.historyWriter.write(player.action + ',')
                # self.historyWriter(' ,')
        else:
            for player in self.players:
                self.parameterObj.historyWriter.write(player.__str__() + ',' + player.value.__str__() + ',')
                if player.value < 22:
                    if self.dealer.value > player.value:
                        self.parameterObj.historyWriter.write('L,')
                    elif self.dealer.value == player.value:
                        self.parameterObj.historyWriter.write('P,')
                    else:
                        self.parameterObj.historyWriter.write('W,')
                else:
                    self.parameterObj.historyWriter.write('L,')
                ##################
                # need to be fixed
                ##################
                self.parameterObj.historyWriter.write(player.action + ',')
                # self.historyWriter(' ,')

    def hit_to_hard_17(self, playerOrHealer):
        while playerOrHealer.value <= 17 and self.i < self.parameterObj.shoe_num * 52:
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
        cardValueStr = self.shoe.cards[self.i].value
        self.cardCountObj.count_card(cardValueStr)
        self.i += 1

    def write_count(self):
        remain_deck = math.ceil((len(self.shoe.cards) - self.i) / 52)
        if remain_deck != 0:
            self.cardCountObj.HiLoTrue = self.cardCountObj.HiLo // remain_deck
            self.cardCountObj.HiOptITrue = self.cardCountObj.HiOptI // remain_deck
            self.cardCountObj.HiOptIITrue = self.cardCountObj.HiOptII // remain_deck
            self.cardCountObj.KOTrue = self.cardCountObj.KO // remain_deck
            self.cardCountObj.OmegaIITrue = self.cardCountObj.OmegaII // remain_deck
            self.cardCountObj.HalvesTrue = self.cardCountObj.Halves // remain_deck
            self.cardCountObj.ZenCountTrue = self.cardCountObj.Halves // remain_deck
        else:
            self.cardCountObj.HiLoTrue = self.cardCountObj.HiLo
            self.cardCountObj.HiOptITrue = self.cardCountObj.HiOptI
            self.cardCountObj.HiOptIITrue = self.cardCountObj.HiOptII
            self.cardCountObj.KOTrue = self.cardCountObj.KO
            self.cardCountObj.OmegaIITrue = self.cardCountObj.OmegaII
            self.cardCountObj.HalvesTrue = self.cardCountObj.Halves
            self.cardCountObj.ZenCountTrue = self.cardCountObj.Halves

        # write count and remaining cards in shoe in history file
        self.parameterObj.historyWriter.write(self.cardCountObj.HiLo.__str__() + ','
                                              + self.cardCountObj.HiLoTrue.__str__() + ','
                                              + self.cardCountObj.HiOptI.__str__() + ','
                                              + self.cardCountObj.HiOptITrue.__str__() + ','
                                              + self.cardCountObj.HiOptII.__str__() + ','
                                              + self.cardCountObj.HiOptIITrue.__str__() + ','
                                              + self.cardCountObj.KO.__str__() + ','
                                              + self.cardCountObj.KOTrue.__str__() + ','
                                              + self.cardCountObj.OmegaII.__str__() + ','
                                              + self.cardCountObj.OmegaIITrue.__str__() + ','
                                              + self.cardCountObj.Halves.__str__() + ','
                                              + self.cardCountObj.HalvesTrue.__str__() + ','
                                              + self.cardCountObj.ZenCount.__str__() + ','
                                              + self.cardCountObj.ZenCountTrue.__str__() + ','
                                              + (len(self.shoe.cards) - self.i).__str__() + ', \n')

    # def find_strategy(self, player_hand, dealer_top_hand):
    #     player_hand_and_index = self.data_frame.to_dict().get('Player Hand')
    #     reversed_dict = dict(map(reversed, player_hand_and_index.items()))
    #     index = reversed_dict.get(player_hand)
    #     return self.data_frame[dealer_top_hand][index]
