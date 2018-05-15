from classes.Board import Board
from copy import copy, deepcopy
import random

class Random:
    def __init__(self, board):
        """
        Takes all information of the board with it's state as the beginning of the game.
        """
        self.board = board

    def randomSelection(self, maxMoves):
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

        while self.board.checkSolution() != 0 and len(visited) < maxMoves:

            children = self.board.createChildren()

            self.board.changeable = random.choice(children)
            visited.append(self.board.changeable)

        print("random we have found it in {} steps".format(len(visited)))
        return visited

    def semiRandomSelection(self, maxMoves):
        """
        Looks for all moves possible and randomly choses one until solved, without
        back to board configurations visited before. If it can't find a move to
        go to a board configuarion that it has been before it goes to a random visited
        (Later added if a configuration has no non-visited options, skip that one.
            i hoped the code would find a solution faster )
        """

        steps = 0
        child = []
        visited = []
        noOptions = []
        path = []

        while self.board.checkSolution() != 0 and len(path) < maxMoves:
            steps += 1
            children = []
            posMoves = self.board.checkPossibleMoves()

            children = self.board.createChildren()

            self.board.changeable = random.choice(children)
            if self.board.changeable not in visited:
                visited.append(self.board.changeable)
                path.append(self.board.changeable)
            else:
                j = 0
<<<<<<< HEAD
                if self.board.changeable not in visited:
                    visited.append(self.board.changeable)
                    path.append(self.board.changeable)
                else:
                    while self.board.changeable in visited:

                        self.board.changeable = random.choice(children)
                        j += 1
                        if j > 20:
                            path = []
                            print("we have made a jump")
                            if self.board.changeable not in noOptions:
                                noOptions.append(self.board.changeable)
                            for element in visited:
                                path.append(element)
                                if element not in noOptions:
                                    self.board.changeable = element
                                break
                        break
        return path
=======
                while self.board.changeable in visited:
                    self.board.changeable = random.choice(children)
                    j += 1
                    if j > 20:
                        path = []
                        print("we have made a jump")
                        if self.board.changeable not in noOptions:
                            noOptions.append(self.board.changeable)
                        for element in visited:
                            path.append(element)
                            if element not in noOptions:
                                self.board.changeable = element
                            break
                    break
                path.append(self.board.changeable)
        return path
>>>>>>> 3a6d6a90d33f0dc71b18cbe50fbf3d6210023e76
