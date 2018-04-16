from miniMax import *
import sys
import random
from util import *

def go():  # go runs the tic tac toe game
    bot = BotStarter()
    parser = BotParser(bot)
    parser.run()


class BotStarter:
    def __init__(self):  # inital state where you internalize random number generator, param self
        self.mm = miniMax()

    def doMove(self, state):  # does a move in the tic tac toe board, param self + state
        moves = state.getField().getAvailableMoves()  # get the available moves on the board set it equal to moves
        #print("I am here.")
        if (len(moves) > 0):
            return self.mm.search(1,1)
        else:
            return None


if __name__ == '__main__':
    go()
