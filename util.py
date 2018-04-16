import sys
import copy

class Field:

    def setMicroBoard(self, xpos, ypos, pId):
        self.__mBoard[xpos][ypos] = pId

    def setMacroBoard(self,xpos,ypos,pId):
        self.__mMacroboard[xpos][ypos] = pId


    def __init__(self):  # init starts the game param self
        self.__EMPTY_FIELD = "."
        self.__AVAILABLE_FIELD = "-1"
        self.__NUM_COLS = 9
        self.__NUM_ROWS = 9
        self.__mBoard = []
        self.__mMacroboard = []  # larger board of tic tac toe
        self.__myId = 0
        self. __opponentId = 0
        null_row = []

        for col in range(self.__NUM_COLS):  # goes through the number of collumns
            null_row.append(self
                            .__EMPTY_FIELD)
        for row in range(self.__NUM_ROWS):  # goes through the rows
            self.__mBoard.append(list(null_row))

        # Macroboard larger board
        null_row = []
        for col in range(self.__NUM_COLS // 3):  # floor division by 3
            null_row.append(self
                            .__EMPTY_FIELD)
        for row in range(self.__NUM_ROWS // 3):
            self.__mMacroboard.append(list(null_row))

    #
    def parseFromString(self, s):  # go through the small board strings parse, parameter s and self
        s = s.replace(";", ",")  # replaces ; with , in s
        r = s.split(",")  # breaks up data from s by the ,
        counter = 0
        for y in range(self.__NUM_ROWS):
            for x in range(self.__NUM_COLS):  # for y in range of the num Rows X rand num cols
                self.__mBoard[x][y] = r[counter]
                counter += 1

    def parseMacroboardFromString(self, s):  # go through larger board parse the strings, parameter s and self
        r = s.split(",")
        counter = 0
        for y in range(3):
            for x in range(3):
                self.__mMacroboard[x][y] = r[counter]
                counter += 1

    def getAvailableMoves(self):  # when you make a move each row and column
        moves = []
        for y in range(self.__NUM_ROWS):
            for x in range(self.__NUM_COLS):
                if (self.isInActiveMicroboard(x, y) and (self.__mBoard[x][y] == self
                        .__EMPTY_FIELD)):
                    moves.append(Move(x, y))
        return moves

    def isInActiveMicroboard(self, x,
                             y):  # param x and y and self.  Checks to see if currently in microboard not finished
        return self.__mMacroboard[x // 3][y // 3] == self.__AVAILABLE_FIELD

    def toString(
            self):  # param self goes through the board and converts it to string puts , in between each x y. param self
        r = ""
        counter = 0
        for y in range(self.__NUM_ROWS):
            for x in range(self.__NUM_COLS):
                if (counter > 0):
                    r += ","
                r += self.__mBoard[x][y]
                counter += 1
        return r

    def isFull(self):  # if there is an empty field then board not full, param self
        for y in range(self.__NUM_ROWS):
            for x in range(self.__NUM_COLS):
                if (self.__mBoard[x][y] == self
                        .__EMPTY_FIELD):  return False
        return True

    def isEmpty(self):  # param self, if board is empty return true
        for y in range(self.__NUM_ROWS):
            for x in range(self.__NUM_COLS):
                if (self.__mBoard[x][y] != self
                        .__EMPTY_FIELD):  return False
        return True

    def getNrColumns(self):  # gets the number of columns in board, param self
        return self.__NUM_COLS

    def getNrRows(self):  # param self, gets the number of rows in board
        return self.__NUM_ROWS

    def getPlayerID(self, x, y):  # param self, x, y: gets the player ID from the small board
        return self.__mBoard[x][y]

    def getMyId(self):  # returns myId variable, param self
        return self.__myId

    def setMyId(self, id):  # sets myId variable equal to param id, param: self, id
        self.__myId = id

    def getOpponentId(self):  # returns opponent Id variable, param self
        return self.__opponentId

    def setOpponentId(self, id):  # sets oppoent ID to id param, param: self, id
        self.__opponentId = id

    def player1Won(self, x,y):  # checks if @ given index if player 1 has one that space in macro board
        if self.__mMacroboard[x][y] == 1:
            return True

    def player0Won(self, x,y):  # checks if player zero has won the macro board
        if self.__mMacroboard[x][y] == 0:
            return True

    def macroHorWin(self):  # returns true if there is a horizontal win
        if (self.player1Won(0,0) and self.player1Won(0,1) and self.player1Won(0,2)) or (
                self.player1Won(1,0) and self.player1Won(1,1) and self.player1Won(1,2)) or (
                self.player1Won(2,0) and self.player1Won(2,1) and self.player1Won(2,2)):
            return 1
        elif (self.player0Won(0,0) and self.player0Won(0,1) and self.player0Won(0,2)) or (
                self.player0Won(1,0) and self.player0Won(1,1) and self.player0Won(1,2)) or (
                self.player0Won(2,0) and self.player0Won(2,1) and self.player0Won(2,2)):
            return 0
        else:
            return False

    def macroVerWin(self):
        if (self.player1Won(0,0) and self.player1Won(1,0) and self.player1Won(2,0)) or (
                self.player1Won(0,1) and self.player1Won(1,1) and self.player1Won(2,1)) or (
                self.player1Won(0,2) and self.player1Won(1,2) and self.player1Won(2,2)):
            return 1
        elif (self.player0Won(0,0) and self.player0Won(1,0) and self.player0Won(2,0)) or (
                self.player0Won(0,1) and self.player0Won(1,1) and self.player0Won(2,1)) or (
                self.player0Won(0,2) and self.player0Won(1,2) and self.player0Won(2,2)):
            return 0
        else:
            return False

    def macroDiagWin(self):
        if (self.player1Won(0,0) and self.player1Won(1,1) and self.player1Won(2,2)) or (
                self.player1Won(0,2) and self.player1Won(1,1) and self.player1Won(2,0)):
            return 1
        elif (self.player0Won(0,0) and self.player0Won(1,1) and self.player0Won(2,2)) or (
                self.player0Won(0,2) and self.player0Won(1,1) and self.player0Won(2,0)):
            return 0
        else:
            return False

    def macroWin(self):
        if self.macroDiagWin() == 1 or self.macroHorWin() == 1 or self.macroVerWin() == 1:
            return 1
        elif self.macroDiagWin() == 0 or self.macroHorWin() == 0 or self.macroVerWin() == 0:
            return 0
        else:
            return False

    def horizontalWin(self,board, xpos, ypos, pId):  # checks if the micro board has been won horizontally
        board[xpos][ypos]
        if ypos % 3 == 0:
            if (self.__mBoard[xpos][ypos] == pId) and (self.__mBoard[xpos][ypos+1] == pId) and (self.__mBoard[xpos][
            ypos+2] == pId):
                return True
            else:
             return False


    def verticalWin(self,board, xpos, ypos, pId):  # checks if the micro board has been won vertically
       board[xpos][ypos]
       if ypos ==0 or ypos==1 or ypos ==2:
        if self.__mBoard[xpos][ypos] == pId and self.__mBoard[xpos][ypos + 3] == pId and self.__mBoard[xpos][
                ypos + 6] == pId:
            return True
        else:
            return False


    def diagonalWinLeft(self,board, xpos, ypos, pId):  # need to include other diagonal as well from top left to bottom right
        __mBoard =board
        if  ypos % 3 == 0 and ypos!=6:
            if __mBoard[xpos][ypos] == pId and __mBoard[xpos][ypos + 4] == pId and __mBoard[xpos][
                    ypos+8] == pId:
                return True
            else:
                return False


    def diagonalWinRight(self,board, xpos, ypos, pId):  # checks if win condition from bottom left to top right
        __mBoard=board
        if ypos==2:
         if __mBoard[xpos][ypos] == pId and __mBoard[xpos][ypos+2] == pId and __mBoard[xpos][ypos+4] == pId:
            return True
         else:
            return False


    def overallDiagonalWin(self,board, xpos, ypos, pId):  # check if diagonal win
        board[xpos][ypos]
        if self.diagonalWinLeft(board,xpos, ypos, pId) or self.diagonalWinRight(board,xpos, ypos+2, pId):
            return True
        else:
            return False


    def middleSquareWon(self, pId):  # checks if the middle square was won
        if (self.horizontalWin(4, 0, pId) or self.horizontalWin(4, 3, pId) or self.horizontalWin(4, 6, pId)) or (
            self.verticalWin(4, 0, pId) or self.verticalWin(4, 1, pId) or self.verticalWin(4,2, pId)) or (
    self.overallDiagonalWin(4, 0, pId)):
            return True
        else:
            return False


    def topLeftWon(self, pId):  # checks if the top left square has been won
        if (self.horizontalWin(0, 0, pId) or self.horizontalWin(0, 3, pId) or self.horizontalWin(0, 6,pId)) or (
            self.verticalWin(0, 0, pId) or self.verticalWin(0, 1, pId) or self.verticalWin(0, 2,pId)) or (
    self.overallDiagonalWin(0, 0, pId)):
           return True
        else:
            return False


    def topRightWon(self, pId):  # checks if the top right board has been won
        if (self.horizontalWin(3, 0, pId) or self.horizontalWin(3, 3, pId) or self.horizontalWin(3, 6, pId)) or (
            self.verticalWin(3, 0, pId) or self.verticalWin(3, 1, pId) or self.verticalWin(3, 2,pId)) or (
        self.overallDiagonalWin(3, 0, pId)):
         return True
        else:
            return False


    def bottomLeftWon(self, pId):  # checks if the bottom left board has been won
        if (self.horizontalWin(6, 0, pId) or self.horizontalWin(6, 3, pId) or self.horizontalWin(6, 6, pId)) or (
            self.verticalWin(6, 0, pId) or self.verticalWin(6, 1, pId) or self.verticalWin(6, 2, pId)) or (
    self.overallDiagonalWin(6, 0, pId)):
            return True
        else:
            return False


    def bottomRightWon(self, pId):
        if (self.horizontalWin(8, 0, pId) or self.horizontalWin(8, 3, pId) or self.horizontalWin(8, 6, pId)) or (
            self.verticalWin(8, 0, pId) or self.verticalWin(8, 1, pId) or self.verticalWin(8, 2, pId)) or (
            self.overallDiagonalWin(8,0,pId)):
            return True
        else:
            return False


    def nextToHor(self,board, xpos, ypos, pId):  # checks if two spaces are next to each other horizontally
        __mBoard = board
        if (ypos ==0): #__EMPTY_FIELD
            if (__mBoard[xpos][0]== pId and __mBoard[xpos][1]==".") or (__mBoard[xpos][0]=="."  and __mBoard[xpos][1]==pId):
                return True
        elif (ypos==1):
            if(__mBoard[xpos][1]==pId and __mBoard[xpos][2]==".")  or (__mBoard[xpos][1] == "." and __mBoard[xpos][2] == pId) or \
              (__mBoard[xpos][1] == pId and __mBoard[xpos][0] == __mBoard
                      .__EMPTY_FIELD) or (__mBoard[xpos][1] == "." and __mBoard[xpos][0] == pId):
                return True
        elif (ypos==2):
            if  (__mBoard[xpos][1]=="." and __mBoard[xpos][2]==pId) or (__mBoard[xpos][1]==pId and __mBoard[xpos][2]=="."):
                return True
        elif (ypos==3):
            if  (__mBoard[xpos][3]=="." and __mBoard[xpos][4]==pId) or (__mBoard[xpos][3]==pId and __mBoard[xpos][4]=="."):
                return True
        elif (ypos==4):
            if (__mBoard[xpos][3] == "." and __mBoard[xpos][4] == pId) or (__mBoard[xpos][3] == pId and __mBoard[xpos][4] == ".") or \
               (__mBoard[xpos][5] == "." and __mBoard[xpos][4] == pId) or (__mBoard[xpos][5] == pId and __mBoard[xpos][4] == "."):
                return True
        elif (ypos==5):
            if  (__mBoard[xpos][5]=="." and __mBoard[xpos][4]==pId) or (__mBoard[xpos][5]==pId and __mBoard[xpos][4]=="."):
                return True
        elif (ypos==6):
            if  (__mBoard[xpos][6]=="." and __mBoard[xpos][7]==pId) or (__mBoard[xpos][6]==pId and __mBoard[xpos][7]=="."):
                return True
        elif (ypos==7):
            if (__mBoard[xpos][6] =="." and __mBoard[xpos][7] == pId) or (__mBoard[xpos][6] =="." and __mBoard[xpos][7] == pId) or \
               (__mBoard[xpos][8] =="." and __mBoard[xpos][7] == pId) or (__mBoard[xpos][8] ==pId and __mBoard[xpos][7] == "."):
                return True
        elif (ypos==8):
            if (__mBoard[xpos][8]=="." and __mBoard[xpos][7]==pId) or (__mBoard[xpos][8]==pId and __mBoard[xpos][7]=="."):
                return True

    def nextToVert(self,board, xpos, ypos, pId):  # checks if two spaces are vertiacally next to each other
        __mBoard = board
        if (ypos==0):
            if (__mBoard[xpos][0]=="." and __mBoard[xpos][3]==pId) or (__mBoard[xpos][0]==pId and __mBoard[xpos][3]=="."):
                return True
        elif (ypos==1):
            if (__mBoard[xpos][1] == "." and __mBoard[xpos][4] == pId)or (__mBoard[xpos][1] ==pId and __mBoard[xpos][4] == "."):
                return True
        elif (ypos==2):
            if  (__mBoard[xpos][2] == "." and __mBoard[xpos][5] == pId) or (__mBoard[xpos][2] ==pId and __mBoard[xpos][5] == "."):
                return True
        elif (ypos==3):
            if (__mBoard[xpos][0] == "." and __mBoard[xpos][3] == pId)  or (__mBoard[xpos][0] == pId and __mBoard[xpos][3] == ".") or \
               (__mBoard[xpos][3] == "." and __mBoard[xpos][6] == pId)  or (__mBoard[xpos][3] == pId and __mBoard[xpos][6] == ".")  :
                return True
        elif (ypos==4):
            if (__mBoard[xpos][1] == "." and __mBoard[xpos][4] == pId) or (__mBoard[xpos][1] == pId and __mBoard[xpos][4] == ".") or \
               (__mBoard[xpos][7] == "." and __mBoard[xpos][4] == pId) or (__mBoard[xpos][7] == pId and __mBoard[xpos][4] == "."):
                return True
        elif (ypos==5):
            if (__mBoard[xpos][2] == "." and __mBoard[xpos][5] == pId) or (__mBoard[xpos][2] == pId and __mBoard[xpos][5] == ".") or \
               (__mBoard[xpos][8] == "." and __mBoard[xpos][5] == pId) or (__mBoard[xpos][8] == pId and __mBoard[xpos][5] == "." )  :
                return True
        elif (ypos ==6):
            if (__mBoard[xpos][3] == "." and __mBoard[xpos][6] == pId) or(__mBoard[xpos][3] == pId and __mBoard[xpos][6] == ".") :
                return True
        elif (ypos==7):
            if (__mBoard[xpos][7] == pId and __mBoard[xpos][4] == ".") or (__mBoard[xpos][7] == "." and __mBoard[xpos][4] ==pId):
                return True
        elif (ypos==8):
            if  (__mBoard[xpos][8] == "." and __mBoard[xpos][5] == pId) or (__mBoard[xpos][8] == pId and __mBoard[xpos][5] == "."):
                return True

    def nextToDiag(self,board, xpos, ypos, pId):  # checks if two squares are diagonally next to each other
       __mBoard = board
       if (ypos ==0):
           if  (__mBoard[xpos][0] =="." and __mBoard[xpos][4] == pId) or (__mBoard[xpos][0] == pId and __mBoard[xpos][4] ==".") :
               return True
       elif (ypos==2):
            if  (__mBoard[xpos][2] == "." and __mBoard[xpos][4] == pId) or (self.__mBoard[xpos][2] == pId and self.__mBoard[xpos][4] == ".") :
                return True
       elif (ypos==4):
           if (__mBoard[xpos][0] =="." and __mBoard[xpos][4] == pId) or (__mBoard[xpos][0] == pId and __mBoard[xpos][4] ==".")  or \
              (__mBoard[xpos][2] =="." and __mBoard[xpos][4] == pId) or (__mBoard[xpos][2] == pId and __mBoard[xpos][4] ==".")  or \
              (__mBoard[xpos][6] =="." and __mBoard[xpos][4] == pId) or (__mBoard[xpos][6] == pId and __mBoard[xpos][4] ==".") or \
              (__mBoard[xpos][8] =="." and __mBoard[xpos][4] == pId) or (__mBoard[xpos][8] == pId and __mBoard[xpos][4] =="."):
               return True
       elif (ypos==6):
           if  (__mBoard[xpos][6] =="."  and __mBoard[xpos][4] == pId)or (__mBoard[xpos][6] == pId  and __mBoard[xpos][4] =="."):
               return True
       elif (ypos ==8):
           if (__mBoard[xpos][8] =="."  and __mBoard[xpos][4] == pId) or (__mBoard[xpos][8] == pId  and __mBoard[xpos][4] =="."):
               return True
    def overallNextTo(self,board, xpos, ypos, pId):  # checks if two squares are next to each other calling the other check functions
        board[xpos][ypos]
        if (self.nextToHor(board,xpos, ypos, pId) or self.nextToVert(board,xpos, ypos, pId) or self.nextToDiag(board,xpos, ypos, pId)):
         return True

    def adjacentSpacesFilled(self,board,xpos,ypos,pId):#checks to see if the empty square is next to two filled squares
        __mBoard = board
        if ypos ==0:
            if (__mBoard[xpos][0]=="." and __mBoard[xpos][1]==pId) and (__mBoard[xpos][0]=="." and __mBoard[xpos][2]==pId)  or (__mBoard[xpos][0]=="." and __mBoard[xpos][3]==pId) and (__mBoard[xpos][0]=="." and __mBoard[xpos][6]==pId):
                return True
        elif ypos==1:
            if (__mBoard[xpos][0]==pId and __mBoard[xpos][1]==".") and (__mBoard[xpos][2]==pId and __mBoard[xpos][1]==".") or (__mBoard[xpos][4]==pId and __mBoard[xpos][1]==".") and (__mBoard[xpos][7]==pId and __mBoard[xpos][1]=="."):
                return True
        elif ypos==2:
            if (__mBoard[xpos][2]=="." and __mBoard[xpos][1]==pId) and (__mBoard[xpos][2]=="." and __mBoard[xpos][0]==pId) or (__mBoard[xpos][2]=="." and __mBoard[xpos][5]==pId) and (__mBoard[xpos][2]=="." and __mBoard[xpos][8]==pId):
                return True
        elif ypos==3:
            if (__mBoard[xpos][0]==pId and __mBoard[xpos][3]==".") and (__mBoard[xpos][6]==pId and __mBoard[xpos][3]==".") or (__mBoard[xpos][4]==pId and __mBoard[xpos][3]==".") and (__mBoard[xpos][5]==pId and __mBoard[xpos][3]=="."):
                return True
        elif ypos==5:
            if (__mBoard[xpos][2]==pId and __mBoard[xpos][5]==".") and (__mBoard[xpos][8]==pId and __mBoard[xpos][5]==".") or (__mBoard[xpos][4]==pId and __mBoard[xpos][5]==".") and(__mBoard[xpos][3]==pId and __mBoard[xpos][5]==".") :
                return True
        elif ypos==6:
            if (__mBoard[xpos][6]==pId and __mBoard[xpos][3]==".") and (__mBoard[xpos][6]==pId and __mBoard[xpos][0]==".") or (__mBoard[xpos][6]=="." and __mBoard[xpos][7]==pId) and (__mBoard[xpos][6]=="." and __mBoard[xpos][8]==pId) or (__mBoard[xpos][6]=="." and __mBoard[xpos][4]==pId) and (__mBoard[xpos][6]=="." and __mBoard[xpos][2]==pId):
                return True
        elif ypos==7:
            if (__mBoard[xpos][8]==pId and __mBoard[xpos][7]==".") and (__mBoard[xpos][7]=="." and __mBoard[xpos][6]==pId) or (__mBoard[xpos][7]=="." and __mBoard[xpos][4]==pId) and (__mBoard[xpos][7]=="." and __mBoard[xpos][1]==pId):
                return True
        elif ypos==8:
            if (__mBoard[xpos][8]=="." and __mBoard[xpos][5]==pId) and (__mBoard[xpos][8]=="." and __mBoard[xpos][2]==pId) or (__mBoard[xpos][8]=="." and __mBoard[xpos][7]==pId) and (__mBoard[xpos][8]=="." and __mBoard[xpos][6]==pId) or (__mBoard[xpos][8]=="." and __mBoard[xpos][4]==pId) and (__mBoard[xpos][8]=="." and __mBoard[xpos][0]==pId):
                return True
        elif ypos==4:
            if (__mBoard[xpos][4] == "." and __mBoard[xpos][1] == pId) and (__mBoard[xpos][4] == "." and __mBoard[xpos][7] == pId) or (__mBoard[xpos][4] == "." and __mBoard[xpos][3] == pId) and (__mBoard[xpos][4] == "." and __mBoard[xpos][5] == pId) or (__mBoard[xpos][4] == "." and __mBoard[xpos][2]==pId) and \
                    (__mBoard[xpos][4]=="." and __mBoard[xpos][6]==pId) or (__mBoard[xpos][4] == "." and __mBoard[xpos][0] == pId) and (__mBoard[xpos][4]=="." and __mBoard[xpos][8]==pId):
                return True

    def movesToWin(self,board, xpos, ypos, pId): #checks how many moves it will take to win a given micro board
        board[xpos][ypos]
        if self.overallDiagonalWin(board,xpos,ypos,pId) or self.verticalWin(board,xpos, ypos,pId) or self.horizontalWin(board,xpos, ypos,pId):
            return 0
        elif  self.adjacentSpacesFilled(board,xpos,ypos,pId):#self.overallNextTo(board,xpos, ypos, pId)and
            return 1#for next to two squares
        elif not(self.overallNextTo(board,xpos, ypos, pId)):
            return 3 #for squares next to blank spaces
        else:
            return 2

    def getMicroBoard(self): #gets the micro board
        return self.__mBoard

    def getMacroBoard(self): #gets the macro board
        return self.__mMacroboard

    def moveTopLeft(self): #checks to see if we have to move on the top right of the board
        if self.__mMacroboard[0][0]==-1:
            return True
        else:
            return False

    def moveTopMid(self): # checks to see if we have to move top middle
        if self.__mMacroboard[0][1]==-1:
            return True
        else:
            return False
    def moveTopRight(self): #checks to see if we need to move in the top right board
        if self.__mMacroboard[0][2]==-1:
            return True
        else:
            return False

    def moveLeftMiddle(self):#checks to see if we need to move middle left
        if self.__mMacroboard[1][0]==-1:
            return True
        else:
            return False
    def moveRightMiddle(self): #checks to see if we need to move middle right
        if self.__mMacroboard[1][2]==-1:
            return True
        else:
            return False

    def moveMiddle(self): #cheks to see if we have to move in the middle square
        if self.__mMacroboard[1][1]==-1:
            return True
        else:
            return False

    def moveBottomLeft(self):# checks to see if we have to move in the bottom left square
        if self.__mMacroboard[2][0]==-1:
            return True
        else:
            return False

    def moveBottomRight(self): #checks to see if we have to move in the bottom right square
        if self.__mMacroboard[2][2]==-1:
            return True
        else:
            return False

    def moveBottomMiddle(self): #checks to see if we are moving bottom middle
        if self.__mMacroboard[2][1]==-1:
            return True
        else:
            return False

    def moveTopMiddle(self): # checks to see if we have to move in the top middle square
        if self.__mMacroboard[0][1]==-1:
            return True
        else:
            return False

    def moveMidLeft(self):#checks to see if we have to move mid left
        if self.__mMacroboard[1][0]==-1:
            return True
        else:
            return False

    def moveMidRight(self):#checks to see if we have move mid right
        if self.__mMacroboard[1][2]==-1:
            return True
        else:
            return False

    def moveBottomMiddle(self):#checks to see if we have to move bottom middle
        if self.__mMacroboard[2][1]==-1:
            return True
        else:
            return False
        # _ hint that name is private by programer, leave alone
        # __  change name of variable, harder to make colision -> similar variable names


class Move:  # move class showing how you can move in ultimate tic tac toe
    __x = -1
    __y = -1

    def __init__(self, x, y):  # initial state, param self,x,y
        self.__x = x
        self.__y = y

    def getX(self):  # get the X var in move, param self
        return self.__x

    def getY(self):  # get the y var in move, param self
        return self.__y

    def toString(self):  # places move so that {x} {y}
        return "place_move {} {}".format(self.__x, self.__y)  # formats x into first {} then y into second {}


class Player:  # player class with empty name
    __name = ""

    def __init__(self, name):  # inital state of player, param self and name, inital name empty
        self.__name = name


class BotState:  # class that describes the state of the bots in the program
    __MAX_TIMEBANK = -1  # set the max time overall for the bots
    __TIME_PER_MOVE = -1  # max time per move for the bots

    __roundNumber = -1
    __moveNumber = -1

    __timebank = -1  # overall time for the bots
    __myName = ""
    __players = {}

    __field = None

    def __init__(self):  # initial state with empty players list
        self.__field = Field()  # sets and calls Field constructor
        self.__players = {}

    def copy(self): # copys the field class
        newField = Field()
        newField.__mBoard=self.__mBoard[:]
        newField.__mMacroBoard = self.__mMacroBoard[:]
        newField.__myId = self.__myId
        newField.__opponentId = self.__opponentId
        return newField


    def setTimebank(self, value):  # sets the timebank for the bots equal to the value passed in, param value and self
        self.__timebank = value

    def setMaxTimebank(self, value):  # param value and self, set the max time bank for the bot equal to the value
        self.__MAX_TIMEBANK = value

    def setTimePerMove(self, value):  # param value and self, sets the time per move allowed equal to value
        self.__TIME_PER_MOVE = value

    def setMyName(self, myName):  # param self and myName, sets name of the player equal to myName
        self.__myName = myName

    def setRoundNumber(self, roundNumber):  # param self, roundNumber, sets the round number currently on
        self.__roundNumber = roundNumber

    def setMoveNumber(self, moveNumber):  # param self, moveNumber, sets the move number equal to moveNumber passed in
        self.__moveNumber = moveNumber

    def getTimebank(self):  # get the available time bank, param self
        return self.__timebank

    def getRoundNumber(self):  # gets the round number currently we are on, param self
        return self.__roundNumber

    def getMoveNumber(self):  # returns move number, param self
        return self.__moveNumber

    def getPlayers(self):  # returns the player's list in the game, param self
        return self.__players

    def getField(self):  # returns the field equal to none, param self
        return self.__field

    def getMyName(self):  # gets the name of the player, param self
        return self.__myName

    def getMaxTimebank(self):  # gets the value of the max time bank, param self
        return self.__MAX_TIMEBANK

    def getTimePerMove(self):  # gets time per move, param self
        return self.__TIME_PER_MOVE


class BotParser:  # parser for the actions of the bots
    __bot = None
    __currentState = None
    __log = None

    def __init__(self,
                 bot):  # inital state with bot equal to param bot, currentState equalling bot state, and creation of a log, params: self, bot
        self.__bot = bot
        self.__currentState = BotState()
        self.__log = Log()  # calls log's contructor sets it to log variable -> logs moves

    def output(self,
               msg):  # output of the bots, sends msg to the log, write everything out to the terminal, param: self + msg
        self.__log.write("Sending: " + msg + " to stdout.")
        print(msg)
        sys.stdout.flush()  # gets rid of lingering text that is buffering

    def run(self):  # runs the program and edits the outputs
        while not sys.stdin.closed:  # used for all interpreter input, while interpreter is not closed
            try:
                rawline = sys.stdin.readline()  # reads line from the stdin
                line = rawline.strip()  # gets rid of whitespace in from and at end of the characters
                self.handle_message(line)  # calls handle_message with the message of line
            except EOFError:  # if problem do this
                self.__log.write('EOF')
                self.__log.close()
        return

    def handle_message(self,
                       message):  # param self and message, handles the message received by the bots puts it into a log
        self.__log.write("bot received: {}\n".format(message))  # writes into the log what instructions bot got
        parts = message.split(" ")  # seperates words by the blank spaces
        if not parts:  # if parts empty cannot parse message
            self.__log.write("Unable to parse line (empty)\n")
        elif parts[0] == 'settings':  # if 1st part is settings then
            self.parseSettings(parts[1], parts[2])  # calls parse settings on next two parts
        elif parts[0] == 'update':
            if (parts[1] == "game"):
                self.parseGameData(parts[2], parts[3])  # calls parseGameData method
        elif parts[0] == 'action':
            if (parts[1] == "move"):
                if (len(parts) > 2):
                    self.__currentState.setTimebank(int(parts[2]))
                move = self.__bot.doMove(self.__currentState)
                print("got the output", move)
                print("move is: ", move.toString())
                if move != None:
                    # sys.stdout.write(move.toString())
                    self.output(move.toString())
                else:
                    # sys.stdout.write("pass")
                    self.output("pass")
        else:
            self.__log.write("Unknown command: {} \n".format(message))  # puts message into {}

    def parseSettings(self, key,
                      value):  # param self, key and value, takes the settings of the game and tells the computer about them
        try:
            if key == "timebank":  # if key word is timebank
                time = int(value)  # set time equal to the value, set time banks equal to that value
                self.__currentState.setMaxTimebank(time)
                self.__currentState.setTimebank(time)
            elif key == "time_per_move":  # if key word is time_per move, set the time allowed per move
                self.__currentState.setTimePerMove(int(value))
            elif key == "player_names":  # if key word is player_names, split up the names into list
                playerNames = value.split(",")
                for playerName in playerNames:
                    player = Player(playerName)  # have player equal to one of the names
                    (self.__currentState.getPlayers())[
                        playerName] = player  # gets hash table associate name with number
            elif key == "your_bot":  # sets bot name to the value given
                self.__currentState.setMyName(value)
            elif key == "your_botid":  # sets bot Id
                myId = int(value)
                opponentId = 2 - myId + 1
                self.__currentState.getField().setMyId(myId)  # distinguish between MyId and Opponent ID
                self.__currentState.getField().setOpponentId(opponentId)
            else:  # if it fails
                self.__log.write("Unable to parse settings input with key {}".format(key))
        except:  # if it fails
            self.__log.write("Unable to parse settings value {} for key {}".format(value, key))
            # e.printStackTrace()

    def parseGameData(self, key, value):  # parses the game data into the program, param self key and value
        try:
            if key == "round":  # if key word is round, set the round on equal to value passed in
                self.__currentState.setRoundNumber(int(value))
            elif key == "move":  # set the number of moves equal to value
                self.__currentState.setMoveNumber(int(value))
            elif key == "macroboard":  # gets the large board and parses it based on the value
                self.__currentState.getField().parseMacroboardFromString(value);
            elif key == "field":  # gets the field and parses it from a string
                self.__currentState.getField().parseFromString(value)
            else:
                self.__log.write("Cannot parse game data input with key {}".format(key))
        except:
            self.__log.write("Cannot parse game data value {} for key {}".format(value, key))
            # e.printStackTrace()


class Log:
    __FNAME = "/tmp/bot-log.txt"

    def __init__(self, fname=None):  # param, self and fname
        if (fname == None):
            import os  # able to use operating system functionally

            pid = os.getpid()  # sets pid equal to current process id
            self.__FNAME = "/tmp/bot-log" + str(pid) + ".txt"  # sets file name to string and the process id
        else:
            self.__FNAME = fname

        self.__FILE = open(self.__FNAME, 'w')  # opens the file for writing

    def write(self, msg):  # param self and message, writes msg into __File
        self.__FILE.write(msg)

    def close(self):  # param self, writes closing loge file then closes the file
        self.write("Closing log file.")
        self.__FILE.close()
