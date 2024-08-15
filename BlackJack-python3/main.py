import pandas as pd
import BlackJackMain as bj
from BlackJackMain import BlackJack

shoe_num = 10000
deck_num = 6
player_num = 1
stand_soft17 = False


def setParameters():
    pass


def main():
    # BlackJack(shoe_num, deck_num, player_num, stand_soft17)
    bj = BlackJack()
    bj.play()


if __name__ == '__main__':
    main()
