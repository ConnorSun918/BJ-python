import datetime
import os
import pandas as pd
from game import Game

import card
from hand import Hand


class BlackJack:
    def __init__(self, shoe_num=10, deck_num=6, player_num=1, stand_soft17=False, strategy='no hit'):
        self.shoe_num = shoe_num
        self.deck_num = deck_num
        self.player_num = player_num
        self.stand_soft17 = stand_soft17
        self.strategy = strategy
        self.strategy_df = []

        if self.strategy != 'no hit':
            self.strategy_df = self.find_Strategy()

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

    def find_Strategy(self):
        if self.deck_num > 4:
            if self.stand_soft17:
                pass
            else:
                filename = './Strategy/4-Deck to 8-Deck Blackjack Strategy(hit soft 17).csv'
                return pd.read_csv(filename, delimiter=',')

    def writeHeaders(self):
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

    def play(self):
        self.writeHeaders()
        for shoeCount in range(self.shoe_num):
            g = Game(self.shoe_num, self.deck_num, self.player_num, self.stand_soft17, self.strategy, self.strategy_df,
                     self.historyWriter, self.infoWriter, shoeCount+1)


