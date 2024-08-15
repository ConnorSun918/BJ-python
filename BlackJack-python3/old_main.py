import old_play
import card
from hand import Hand
from old_play import Game
import datetime


def main():
    # time = datetime.datetime.now().strftime("%d %B %Y %I:%M%p")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(time)

    player_num = 1
    shoe_num = 1
    trail_num = 10000
    count_strategy = 'Hi-Lo'

    fileStr = player_num.__str__() + 'player-' + shoe_num.__str__() + 'decks-' + trail_num.__str__() + 'shoes-'

    # count_strategy = 'Hi-Opt I'
    # count_strategy = 'Hi-Opt II'
    # count_strategy = 'KO'
    # count_strategy = 'Omega II'
    # count_strategy = 'Red 7'
    # count_strategy = 'Halves'
    # count_strategy = 'Zen Count'

    dealer = Hand()
    players = [Hand() for c in range(player_num)]

    shoe = card.Shoe(shoe_num)
    # print(shoe)

    infoWriter = open(fileStr + time + 'info.txt', "w")
    historyWriter = open(fileStr + time + 'history.csv', "w")
    # dataWriter = open(fileStr + time + '.csv', 'w')

    infoWriter.write('number of shoe: ' + shoe_num.__str__() + '\n')
    infoWriter.write('number of player: ' + player_num.__str__() + '\n')
    infoWriter.write('number of trail: ' + trail_num.__str__() + '\n')

    # historyWriter.write('shoe#, count value, true count value, remain cards,')
    historyWriter.write('shoe#,')
    historyWriter.write('Hi-Lo, Hi-Lo True, Hi-Opt I, Hi-Opt I True, Hi-Opt II, Hi-Opt II True, KO, KO True, Omega II, '
                        'Omega II True, Halves, Halves True, Zen Count, Zen Count True,')
    historyWriter.write('remain cards,')
    historyWriter.write('dealer hand,dealer value, dealer face card,')
    for i in range(len(players)):
        historyWriter.write('player' + (i + 1).__str__() + ' hand:,' + 'player' + (i + 1).__str__() + ' value:,'
                            + 'player' + (i + 1).__str__() + ' statues:,')
    historyWriter.write('\n')

    for x in range(trail_num):
        shoe.shuffle()
        print('shoe' + (x + 1).__str__() + ': ' + shoe.__str__())
        # historyWriter.write('shoe' + (x + 1).__str__() + '\n')
        # game = Game(shoe, dealer, players, count_strategy, infoWriter, historyWriter, dataWriter, shoe_num, x + 1)
        game = Game(shoe, dealer, players, count_strategy, infoWriter, historyWriter, shoe_num, x + 1)

        game.play()


if __name__ == '__main__':
    main()
