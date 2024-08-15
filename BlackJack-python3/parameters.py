import datetime
import os

import pandas as pd


class parameters:
    def __init__(self, shoe_num=1, deck_num=6, player_num=2, stand_soft17=False,
                 # strategyFileName='./Strategy/4-Deck to 8-Deck Blackjack Strategy(hit soft 17).csv'):
                 strategyFileName='./Strategy/4-Deck to 8-Deck Blackjack Strategy(hit soft 17).csv'):
        self.shoe_num = shoe_num
        self.deck_num = deck_num
        self.player_num = player_num
        self.stand_soft17 = stand_soft17
        self.strategy_df = pd.read_csv(strategyFileName, delimiter=',')

        # set up writers
        time = datetime.datetime.now().strftime("%Y-%m-%d time-%H-%M-%S")
        fileNameStr = str(self.player_num) + 'player-' + str(self.deck_num) + 'decks-' + str(self.shoe_num) \
                      + 'shoes-'
        path = "./result/" + time
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)

        self.historyWriter = open(path + "/" + fileNameStr + 'history.csv', "w")
        self.infoWriter = open(path + "/" + fileNameStr + 'info.txt', "w")

        # write header for history
        self.infoWriter.write('deck(s): ' + self.deck_num.__str__() + '\t')
        self.infoWriter.write('player(s): ' + self.player_num.__str__() + '\t')
        self.infoWriter.write('shoe(s): ' + self.shoe_num.__str__() + '\n')

        # shoe#,dealer hand,dealer value, dealer face card,player1 hand,player1 value,player1 statues,
        # Hi-Lo, Hi-Lo True, Hi-Opt I, Hi-Opt I True, Hi-Opt II, Hi-Opt II True, KO, KO True, Omega II, Omega II True,
        # Halves, Halves True, Zen Count, Zen Count True,remain cards,
        self.historyWriter.write('shoe#,round#,')
        self.historyWriter.write('dealer hand,dealer value,dealer face card,')
        for i in range(self.player_num):
            self.historyWriter.write('player' + (i + 1).__str__() + ' hand,' +
                                     'player' + (i + 1).__str__() + ' value,' +
                                     'player' + (i + 1).__str__() + ' action,' +
                                     'player' + (i + 1).__str__() + ' statues,')
        self.historyWriter.write(
            'Hi-Lo, Hi-Lo True, Hi-Opt I, Hi-Opt I True, Hi-Opt II, Hi-Opt II True, KO, KO True, Omega II, '
            'Omega II True, Halves, Halves True, Zen Count, Zen Count True,')
        self.historyWriter.write('remain cards, \n')

    def find_strategy(self, player_hand, dealerHand):
        dealer_top_hand_num = dealerHand.hand[0].value
        if dealer_top_hand_num == 'A':
            dealer_top_card = 'ACE'
        elif dealer_top_hand_num == '2':
            dealer_top_card = 'TWO'
        elif dealer_top_hand_num == '3':
            dealer_top_card = 'THREE'
        elif dealer_top_hand_num == '4':
            dealer_top_card = 'FOUR'
        elif dealer_top_hand_num == '5':
            dealer_top_card = 'FIVE'
        elif dealer_top_hand_num == '6':
            dealer_top_card = 'SIX'
        elif dealer_top_hand_num == '7':
            dealer_top_card = 'SVEN'
        elif dealer_top_hand_num == '8':
            dealer_top_card = 'EIGHT'
        elif dealer_top_hand_num == '9':
            dealer_top_card = 'NINE'
        elif dealer_top_hand_num == '10':
            dealer_top_card = 'TEN'
        elif dealer_top_hand_num == 'J':
            dealer_top_card = 'TEN'
        elif dealer_top_hand_num == 'Q':
            dealer_top_card = 'TEN'
        elif dealer_top_hand_num == 'K':
            dealer_top_card = 'TEN'
        else:
            print('!!!Error!!!')
            print('in parameters.py - find_find_strategy')
            print('undefined dealer top card')

        print(dealer_top_card)
        print('player_hand: ')
        print(player_hand.hand()[0])
        print(player_hand.get_value())

        player_hand_and_index = self.strategy_df.to_dict().get('Player Hand')
        reversed_dict = dict(map(reversed, player_hand_and_index.items()))
        index = reversed_dict.get(player_hand)
        print('player_hand_and_index: ')
        print(player_hand_and_index)
        print('reversed_dict: ')
        print(reversed_dict)
        print('index: ' + index)
        return self.strategy_df[dealer_top_card][index]

    # def find_strategy(self, player_hand, dealer_top_hand):
    #     player_hand_and_index = self.data_frame.to_dict().get('Player Hand')
    #     reversed_dict = dict(map(reversed, player_hand_and_index.items()))
    #     index = reversed_dict.get(player_hand)
    #     return self.data_frame[dealer_top_hand][index]

    def printAll(self):
        print("shoe_num: " + self.shoe_num.__str__())
        print("deck_num: " + self.deck_num.__str__())
        print("player_num: " + self.player_num.__str__())
        print("stand_soft17: " + self.stand_soft17.__str__())
        print("strategy_df: " + self.strategy_df.__str__())
