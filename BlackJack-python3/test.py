import csv
import pandas as pd
import strategy_handler


def main():
    filename = './Strategy/4-Deck to 8-Deck Blackjack Strategy(hit soft 17).csv'

    # opening the file using "with"
    # statement
    # with open(filename, 'r') as data:
    #
    #     for line in csv.DictReader(data):
    #         print(line)
    #
    # with open('./Strategy/4-Deck to 8-Deck Blackjack Strategy(hit soft 17).csv') as csvDataFile:
    #     csvReader = csv.reader(csvDataFile)
    #     for row in csvReader:
    #         print(row)

    df = pd.read_csv(filename, delimiter=',')
    print(type(df))
    print(df.to_dict())
    print(df.to_dict().keys())
    print(df.to_dict().get('Player Hand'))
    print(df.to_dict().get('Player Hand').items())

    test = df.to_dict().get('Player Hand')
    reversed_dictionary = dict(map(reversed, test.items()))
    print(reversed_dictionary.get('AA'))
    delaerH = 'TWO'
    print(df.to_dict()[delaerH][34])

    # print(df.to_dict().values())

    # strategy_move = sh.


if __name__ == '__main__':
    main()
