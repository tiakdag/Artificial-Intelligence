#!/usr/bin/env python3

import sys
import random
from util import *


# def run():
#     while not sys.stdin.closed:
#         try:
#             rawline = sys.stdin.readline()
#             line = rawline.strip()
#             handle_message(line)
#         except EOFError:
#             sys.stderr.write('EOF')
#     return

# def handle_message(message):
#     sys.stderr.write("bot received: {}\n".format(message))
#     parts = message.split()
#     if not parts:
#         sys.stderr.write("Unable to parse line (empty)\n")
#     elif parts[0] == 'hello':
#         out('hello back')
#     else:
#         sys.stderr.write("Unable to parse line\n")

# def out(message):
#     sys.stdout.write(message + '\n')
#     sys.stdout.flush()

def go():  # go runs the tic tac toe game
    bot = BotStarter()
    parser = BotParser(bot)
    parser.run()


class BotStarter:
    def __init__(self):  # inital state where you internalize random number generator, param self
        random.seed()

    def doMove(self, state):  # does a move in the tic tac toe board, param self + state
        moves = state.getField().getAvailableMoves()  # get the available moves on the board set it equal to moves
        if (len(moves) > 0):  # if length of moves > 0
            return moves[random.randrange(len(moves))]  # randomly selects move from the range of moves
        else:
            return None


if __name__ == '__main__':
    go()
