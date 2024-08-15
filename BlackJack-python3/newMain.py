from cardCount import cardCount
from newGame import newGame
from parameters import parameters


def main():
    parametersObj = parameters()
    # parametersObj.printAll()
    cardCountObj = cardCount()
    for shoeCount in range(parametersObj.shoe_num):
        game = newGame(parametersObj, shoeCount+1)


if __name__ == '__main__':
    main()
