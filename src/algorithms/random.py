
from classes.Board import Board
from copy import copy, deepcopy
import random

class Random:
    def __init__(self, board, archive):
        """
        Takes all information of the board with it's state as the beginning of the game.
        """
        self.board = board
        self.archive = archive
        self.archive.visitedStates[str(self.board.changeable)] = "beginning!"



    def semiRandomSelection(self):
        """
        Looks for all moves possible and randomly choses a state that he hasn't visited each time,
        until solved. If al possible moves are visited states, it goes back one move.
        """

        foldername = "random"


        while self.board.checkSolution() != 0:

            children = self.board.createChildren()
            childToCheck = 0
            amountOfChildren = len(children)

            while childToCheck != amountOfChildren:
                children, childToCheck, amountOfChildren = self.archive.removeRedundantChild(children, childToCheck, amountOfChildren)

            if amountOfChildren > 0:
                child  = random.choice(children)
                self.archive.addToArchive(self.board.changeable, [child])
                self.board.changeable = child
            else:
                self.board.changeable = self.archive.visitedStates[str(self.board.changeable)]

        path = self.pathSolution(self.board.changeable)
        return len(path)

    def pathSolution(self, solutionState):
            """
            Visualizes the path found through breadth first search.
            """
            path = [solutionState]

            child = copy(solutionState)

            parent = self.archive.visitedStates[str(child)]

            while self.archive.visitedStates[str(child)] != "beginning!":
                path.insert(0, parent)

                child = parent
                parent = self.archive.visitedStates[str(child)]

            return path



