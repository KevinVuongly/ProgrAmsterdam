from classes.Board import Board
from copy import copy, deepcopy
import random

class Random:
    def __init__(self, board):
        """
        Takes all information of the board with it's state as the beginning of the game.
        """
        self.board = board

    def randomSelection(self):
        """
        Looks for all moves possible and randomly choses one until solved, without
        back to board configurations visited before. If it can't find a move to
        go to a board configuarion that it has been before it goes to a random visited
        (Later added if a configuration has no non-visited options, skip that one.
            i hoped the code would find a solution faster )
        """
        counter = 0
        child = []
        visited = []
        noOptions = []

        while self.board.checkSolution() != 0:

            counter += 1
            children = self.board.createChildren()

            self.board.changeable = random.choice(children)

        print("WE HAVE FOUND IT!")
        print(counter)
        return self.board

    def semiRandomSelection(self):
        """
        Looks for all moves possible and randomly choses one until solved, without
        back to board configurations visited before. If it can't find a move to
        go to a board configuarion that it has been before it goes to a random visited
        (Later added if a configuration has no non-visited options, skip that one.
            i hoped the code would find a solution faster )
        """
        beginState = deepcopy(self.board.changeable)

        counter = 0
        child = []
        visited = []
        noOptions = []

        while self.board.checkSolution() != 0:
            counter += 1
            children = []
            j = 0
            posMoves = self.board.checkPossibleMoves()

            for i in range(self.board.nrOfCars):
                for move in posMoves[i]:
                    if not move:
                        continue
                    else:
                        child = copy(self.board.changeable)
                        child[i] = child[i] + posMoves[i][j]
                        children.append(child)
                    j += 1
                j = 0
            if not children:
                continue
            else:
                self.board.changeable = random.choice(children)
                j = 0
                if self.board.changeable not in visited:
                    visited.append(self.board.changeable)
                else:
                    while self.board.changeable in visited:

                        self.board.changeable = random.choice(children)
                        j += 1
                        if j > 20:
                            if self.board.changeable not in noOptions:
                                noOptions.append(self.board.changeable)
                            for element in visited:
                                if element not in noOptions:
                                    self.board.changeable = element
                                break
                        break
        print(counter)
        print("WE HAVE FOUND IT!")
        print(visited)
        return self.board