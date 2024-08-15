import pandas as pd


class strategy_handler:
    def __init__(self):
        filename = './Strategy/4-Deck to 8-Deck Blackjack Strategy(hit soft 17).csv'
        self.data_frame = pd.read_csv(filename, delimiter=',')

    def find_strategy(self, player_hand, dealer_top_hand):
        player_hand_and_index = self.data_frame.to_dict().get('Player Hand')
        reversed_dict = dict(map(reversed, player_hand_and_index.items()))
        index = reversed_dict.get(player_hand)
        return self.data_frame[dealer_top_hand][index]


if __name__ == '__main__':
    sh = strategy_handler()
    print(sh.find_strategy('AA', 'TWO'))
