import util as u
import copy
import random

__Field = u.Field()
bestMove = 0
specificPlace = 0
index = 0

util = __Field

'''
__mBoard = []
__mBoard = __Field.getMicroBoard()
__mMacroBoard = []
__mMacroBoard = __Field.getMacroBoard()
'''


class miniMax:  # algorithm class
    gameScore = 0
    minimizeScore = 0
    thePlayer = 0
    #random.seed()
    # move = u.Move(8,8)
    # testNode = Node(util.getMicroBoard(),move)

    def setPlayer(self, player):  # set the player varaible
        self.thePlayer = player
        return self.thePlayer

    def getPlayer(self):  # get the player variable
        return self.thePlayer

    def getMoveScores(self, board, player):  # get the move scores array so that the board can be evaluated
        moveScore = self.factor(board, player)
        return moveScore

    def score(self, player):  # gives a score to the different states of the game
        if player == 1:
            if util.middleSquareWon(1):
                self.gameScore += 50
            if util.topLeftWon(1):
                self.gameScore += 20
            if util.topRightWon(1):
                self.gameScore += 20
            if util.bottomLeftWon(1):
                self.gameScore += 20
            if util.bottomRightWon(1):
                self.gameScore += 20
            if util.macroWin() == 1:
                self.gameScore += 1000
                return self.gameScore
            else:
                return 0

        if player == 0:
            if util.middleSquareWon(0):
                self.minimizeScore -= 50
            if util.topLeftWon(0):
                self.minimizeScore -= 20
            if util.topRightWon(0):
                self.minimizeScore -= 20
            if util.bottomLeftWon(0):
                self.minimizeScore -= 20
            if util.bottomRightWon(0):
                self.minimizeScore -= 20
            if util.macroWin() == 0:
                self.minimizeScore -= 1000
                return self.minimizeScore
            else:
                return 0

    # need to take (1/amount of moves +1 needed to win the board) * board's value add up
    def factor(self, board, player):
        __mBoard = board
        __moveScores = []
        __moveScores.clear()

        if player == 1:
            if util.moveTopLeft():
                for y in range(9):  # go through the microboard
                    if (__mBoard[0][y] == 0):
                        __moveScores.append(-9)
                    elif (__mBoard[0][y] == 1):
                        __moveScores.append(9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 0, y, 1) + 1)) * 20)
                return __moveScores
            elif util.moveTopRight():
                for y in range(9):  # go through the microboard
                    if (__mBoard[2][y] == 0):
                        __moveScores.append(-9)
                    elif (__mBoard[2][y] == 1):
                        __moveScores.append(9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 2, y, 1) + 1)) * 20)
                return __moveScores
            elif util.moveBottomLeft():
                for y in range(9):  # go through the microboard
                    if (__mBoard[6][y] == 0):
                        __moveScores.append(-9)
                    elif (__mBoard[6][y] == 1):
                        __moveScores.append(9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 6, y, 1) + 1)) * 20)
                return __moveScores
            elif util.moveBottomRight():
                for y in range(9):  # go through the microboard
                    if (__mBoard[8][y] == 0):
                        __moveScores.append(-9)
                    elif (__mBoard[8][y] == 1):
                        __moveScores.append(9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 8, y, 1) + 1)) * 20)
                return __moveScores
            elif util.moveMiddle():
                for y in range(9):  # go through the microboard
                    if (__mBoard[4][y] == 0):
                        __moveScores.append(-9)
                    elif (__mBoard[4][y] == 1):
                        __moveScores.append(9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 4, y, 1) + 1)) * 50)
                return __moveScores
            elif util.moveTopMiddle():
                for y in range(9):  # go through the microboard
                    if (__mBoard[1][y] == 0):
                        __moveScores.append(-9)
                    elif (__mBoard[1][y] == 1):
                        __moveScores.append(9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 1, y, 1) + 1)))
                return __moveScores
            elif util.moveLeftMiddle():
                for y in range(9):  # go through the microboard
                    if (__mBoard[3][y] == 0):
                        __moveScores.append(-9)
                    elif (__mBoard[3][y] == 1):
                        __moveScores.append(9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 3, y, 1) + 1)))
                return __moveScores
            elif util.moveRightMiddle():
                for y in range(9):  # go through the microboard
                    if (__mBoard[5][y] == 0):
                        __moveScores.append(-9)
                    elif (__mBoard[5][y] == 1):
                        __moveScores.append(9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 5, y, 1) + 1)))
                return __moveScores
            elif util.moveBottomMiddle():
                for y in range(9):  # go through the microboard
                    if (__mBoard[7][y] == 0):
                        __moveScores.append(-9)
                    elif (__mBoard[7][y] == 1):
                        __moveScores.append(9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 7, y, 1) + 1)))
                return __moveScores
        if player == 0:
            if util.moveTopLeft():
                for y in range(9):  # go through the microboard
                    if (__mBoard[0][y] == 1):
                        __moveScores.append(9)
                    elif (__mBoard[0][y] == 0):
                        __moveScores.append(-9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 0, y, 0) + 1)) * -20)
                return __moveScores
            elif util.moveTopRight():
                for y in range(9):  # go through the microboard
                    if (__mBoard[2][y] == 1):
                        __moveScores.append(9)
                    elif (__mBoard[2][y] == 0):
                        __moveScores.append(-9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 2, y, 0) + 1)) * -20)
                return __moveScores
            elif util.moveTopMiddle():
                for y in range(9):  # go through the microboard
                    if (__mBoard[1][y] == 1):
                        __moveScores.append(9)
                    elif (__mBoard[1][y] == 0):
                        __moveScores.append(-9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 1, y, 0) + 1)))
            elif util.moveBottomLeft():
                for y in range(9):  # go through the microboard
                    if (__mBoard[6][y] == 1):
                        __moveScores.append(9)
                    elif (__mBoard[6][y] == 0):
                        __moveScores.append(-9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 6, y, 0) + 1)) * -20)
                return __moveScores
            elif util.moveBottomRight():
                for y in range(9):  # go through the microboard
                    if (__mBoard[8][y] == 1):
                        __moveScores.append(9)
                    elif (__mBoard[8][y] == 0):
                        __moveScores.append(-9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 8, y, 0) + 1)) * -20)
                return __moveScores
            elif util.moveBottomMiddle():
                for y in range(9):  # go through the microboard
                    if (__mBoard[7][y] == 1):
                        __moveScores.append(9)
                    elif (__mBoard[7][y] == 0):
                        __moveScores.append(-9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 7, y, 0) + 1)))
                return __moveScores
            elif util.moveMiddle():
                for y in range(9):  # go through the microboard
                    if (__mBoard[4][y] == 1):
                        __moveScores.append(9)
                    elif (__mBoard[4][y] == 0):
                        __moveScores.append(-9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 4, y, 0) + 1)) * -50)
                return __moveScores
            elif util.moveLeftMiddle():
                for y in range(9):  # go through the microboard
                    if (__mBoard[6][y] == 1):
                        __moveScores.append(9)
                    elif (__mBoard[6][y] == 0):
                        __moveScores.append(-9)
                    else:
                        __moveScores.append((1 / (util.movesToWin(__mBoard, 6, y, 0) + 1)))
                return __moveScores
            elif util.moveRightMiddle():
                for y in range(9):  # go through the microboard
                    if (__mBoard[6][y] == 1):
                        __moveScores.append(9)
                    elif (__mBoard[6][y] == 0):
                        __moveScores.append(-9)
                    else:
                        __moveScores.append(1 / (util.movesToWin(__mBoard, 6, y, 0) + 1))
                return __moveScores
                # def eval(self,player):
                #    evalNumber = miniMax.factor(self,player)
                #   x= max(evalNumber)
                #  return x

    def eval(self, board, player):  # sums the value of the board
        evalNumber = self.factor(board, player)
        return sum(evalNumber)

    # __move = u.Move(board,value)


    def whichBoard(self):  # returns the x needed to move in the board
        if util.moveTopLeft():
            return 0
        elif util.moveTopRight():
            return 2
        elif util.moveMiddle():
            return 4
        elif util.moveBottomLeft():
            return 6
        elif util.moveBottomRight():
            return 8
        elif util.moveTopMiddle():
            return 1
        elif util.moveMidLeft():
            return 3
        elif util.moveMidRight():
            return 5
        elif util.moveBottomMiddle():
            return 7
        return -1 #TODO FIX 

    def argMax(self, list):  # find the best value and the node at which it occurs
        minVal = -100000000
        for i in range(len(list)):
            node = Node(list[i].getBoard(), list[i].getAction())
            h_miniMax = list[i].getValueOfNode()
            node.setValueNode(h_miniMax)
            if node.getValueOfNode() > minVal:
                best = node
                minVal = node.getValueOfNode()
        return node
    def argMin(self,list):
        maxVal = 100000000
        for i in range(len(list)):
            node = Node(list[i].getBoard(), list[i].getAction())
            h_miniMax = list[i].getValueOfNode()
            node.setValueNode(h_miniMax)
            if node.getValueOfNode() < maxVal:
                min = node
                maxVal = node.getValueOfNode()
            return node

    def search(self, player, depth):  # actual minimax search algorithm here
        # eval to the end leaves when you get depth apply eval function
        counter = 0
        move = u.Move(self.whichBoard(), counter)
        node = Node(util.getMicroBoard(), move)
        if util.macroWin():
            return self.score(player)
        #if util.isEmpty():
         #   moves = util.getAvailableMoves()  # get the available moves on the board set it equal to moves
         #   if (len(moves) > 0):  # if length of moves > 0
         #       return moves[random.randrange(len(moves))]
        children = node.getChildren(player)
        #depth1 = node.childrenDepth1(player)
        numbers = [0, 1, 2, 3, 6]
        nodes = []
        if depth == 0:
            #self.factor(children[self.counter].getBoard(), player)
            # possibleState = children[self.counter].getBoard()
            for nums in numbers:
                horzWin = children[counter].horizontalWin(self.whichBoard(), nums,player)  # Return the player id to give the correct value
                vertWin = children[counter].verticalWin(self.whichBoard(), nums, player)
                diagWin = children[counter].overallDiagonalWin(self.whichBoard(), nums, player)
                if horzWin == 1 or vertWin == 1 or diagWin == 1:
                    children[counter].setValueNode(100)
                    return children[counter]
                elif horzWin == 0 or vertWin == 0 or diagWin == 0:
                    children[counter].setValueNode(-100)
                    return children[counter]
            self.h_miniMax = children[counter].eval()
            children[counter].setValueNode(children[counter].eval())
            return children[counter]
        else:
            if player == 1:
                for a in children:
                    self.setPlayer(1)
                    nodes.append(self.search(0, depth - 1))  # TODO change 1 to zero
                    counter += 1
                bestNode = (self.argMax(nodes))
                xMove = bestNode.getAction().getX()
                yMove = bestNode.getAction().getY()
                fish = u.Move(xMove, yMove)
                return u.Move(xMove, yMove)
            elif player == 0:
                for a in children:
                    self.setPlayer(0)
                    nodes.append(self.search(1,depth-1))
                    self.counter +=1
                smallNode = (self.argMin(nodes))
                xMove = smallNode.getAction().getX()
                yMove = smallNode.getAction().getY()
                return u.Move(xMove,yMove)

    '''
            if util.isEmpty():
                return u.Move(self.whichBoard(),5)
            elif self.whichBoard()== 1 or self.whichBoard()==3 or self.whichBoard()==5 or self.whichBoard()==7:
                if not(testBoard[self.whichBoard()][5]==1) or not(testBoard[self.whichBoard()][5]==0):
                   return u.Move(self.whichBoard(), 5)
                elif not(testBoard[self.whichBoard()][3]==1) or not(testBoard[self.whichBoard()][3]==0):
                    return u.Move(self.whichBoard(),3)
                elif not(testBoard[self.whichBoard()][1]==1) or not(testBoard[self.whichBoard()][1]==0):
                    return u.Move(self.whichBoard(),1)
                elif not(testBoard[self.whichBoard()][7]==1) or not(testBoard[self.whichBoard()][7]==0):
                    return u.Move(self.whichBoard(),7)
            '''

    def isMovesLeft(self, __mBoard):
        for x in range(9):
            for y in range(9):
                if __mBoard[x][y] != 0 or __mBoard[x][y] != 1:
                    return True
        return False

    def findBestMove(self, xpos, ypos, pId):

        for moves in util.getMicroBoard:
            if self.scoreBasedOnMoves(xpos, ypos, pId) > bestMove:
                bestMove = self.scoreBasedOnMoves(xpos, ypos, pId)

        return bestMove


class Node:  # Take in the field class so that for the actions get the available moves
    # h_miniMax = 0  #create a field stores the value of the node call it h_miniMax

    def __init__(self, board, action):  # create the node class
        self.board = board  # if needed, replace with self.board = copy.deepcopy(board)
        self.action = action
        self.h_miniMax = 0

    def getBoard(self):  # get the board in the node
        return self.board

    def setBoard(self, board):  # set the board if needed
        self.board = board

    def setValueNode(self, x):  # set the value of the node
        self.h_miniMax = x

    def getValueOfNode(self):
        return self.h_miniMax

    def getAction(self):  # get the action we took
        return self.action

    def eval(self):  # returns value of how good the board is overall add list to parameters
        mm = miniMax()
        player = mm.getPlayer()
        moveScores = mm.factor(self.getBoard(), player)
        self.setValueNode(sum(moveScores))
        return self.h_miniMax

    def setMove(self, x, y, player):  # places a value into a spot equal to player
        self.board[x][y] = player

    def setAction(self, x, y):
        self.action = u.Move(x, y)

    def childrenDepth1(self,player):
        mm = miniMax()
        specificBoard = mm.whichBoard()
        children = self.getChildren(player)
        fish = len(children)
        for x in range (fish):
            for z in range(9):
                newBoard = copy.deepcopy(children[x].getBoard())
                node = Node(newBoard, self.action)
                if not (self.board[specificBoard][z] == 1 or self.board[specificBoard][z] == 0):
                    node.setMove(specificBoard, z, player)
                    node.setAction(specificBoard, z)
                    children.append(node)  # issue
                # node.setAction(specificBoard,z,".")
        return children
    def getChildren(self, player):  # returns a list of nodes (ie moves i can make)
        mm = miniMax()
        specificBoard = mm.whichBoard()
        children = []
        for z in range(9):
            newBoard = copy.deepcopy(self.board)
            node = Node(newBoard, self.action)
            myX = specificBoard
            myY = z
            if not (self.board[specificBoard][z] == 1 or self.board[specificBoard][z] == 0):
                node.setMove(specificBoard, z, player)
                node.setAction(specificBoard, z)
                children.append(node)  # issue
                # node.setAction(specificBoard,z,".")
        return children

    def horizontalWin(self, xpos, ypos, pId):  # checks if the micro board has been won horizontally
        node = Node(self.getBoard(), self.getAction())
        __mBoard = node.getBoard()
        if ypos % 3 == 0:
            if (__mBoard[xpos][ypos] == pId) and (__mBoard[xpos][ypos + 1] == pId) and (
                __mBoard[xpos][ypos + 2] == pId):
                return pId
            else:
                return "False"

    def verticalWin(self, xpos, ypos, pId):  # checks if the micro board has been won vertically
        node = Node(self.getBoard(), self.getAction())
        __mBoard = node.getBoard()
        if ypos == 0 or ypos == 1 or ypos == 2:
            if __mBoard[xpos][ypos] == pId and __mBoard[xpos][ypos + 3] == pId and __mBoard[xpos][ypos + 6] == pId:
                return pId
            else:
                return "False"

    def diagonalWinLeft(self, xpos, ypos, pId):  # need to include other diagonal as well from top left to bottom right
        node = Node(self.getBoard(), self.getAction())
        __mBoard = node.getBoard()
        if ypos == 0:
            if __mBoard[xpos][ypos] == pId and __mBoard[xpos][ypos + 4] == pId and __mBoard[xpos][ypos + 8] == pId:
                return True
            else:
                return False

    def diagonalWinRight(self, xpos, ypos, pId):  # checks if win condition from bottom left to top right
        node = Node(self.getBoard(), self.getAction())
        __mBoard = node.getBoard()
        if ypos == 2:
            if __mBoard[xpos][ypos] == pId and __mBoard[xpos][ypos + 2] == pId and __mBoard[xpos][
                        ypos + 4] == pId:
                return True
            else:
                return False

    def overallDiagonalWin(self, xpos, ypos, pId):  # check if diagonal win
        if self.diagonalWinLeft(xpos, ypos, pId) or self.diagonalWinRight(xpos, ypos, pId):
            return pId
        else:
            return "False"


if __name__ == '__main__':
    __mBoard = util.getMicroBoard()
    __macroBoard = util.getMacroBoard()
    mm = miniMax()

    util.setMacroBoard(2, 2, -1)
    mm.search(1,1)


'''def miniMax_decision(self,state, pId):
        player = pId
        actions = self.factor(pId)
        def maxValue(self):
            if self.__Field.macroWin()==0 or self.__Field.macroWin()==1:
                return self.scoreBasedOnMoves(pId)
            v = -100000
            for a in actions:
                # v = max(v, min_value(game.result(state, a)))
                return v
        def minValue(self):
            if self.__Field.macroWin() == 0 or self.__Field.macroWin() == 1:
                return self.scoreBasedOnMoves(pId)
            v = 100000
            for a in actions:
                #v = min(v, max_value(game.result(state, a)))
                return v

class Node:  # creates a node class which is every microboard
    def __init__(self, state, parent=None, value=0): # state what mBoard and macroBoard looks like
        self.state = (self.__mBoard, self.__macroBoard)
        self.value = value
        self.depth = 0
        self.children = []
        self.parent = parent
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):  # representation of the node
        return "<Node {}>".format(self.state)

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]
 class Game:
    def actions(self): # returns a list of allowable moves
        return util.getAvailableMoves()

return argmax(game.actions(state),
                  key=lambda a: min_value(game.result(state, a)))

'''