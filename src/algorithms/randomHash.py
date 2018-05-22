from classes.Board import Board
from copy import copy, deepcopy
import random

class Random:
    def __init__(self, board, archive, colors):
        """
        Takes all information of the board with it's state as the beginning of the game.
        """
        self.board = board
        self.archive = archive
        self.archive.visitedStates[str(self.board.changeable)] = "beginning!"


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

            while childToCheck != amountOfChildren:
                children, childToCheck, amountOfChildren = self.archive.removeRedundantChild(children, childToCheck, amountOfChildren)

            child  = random.choice(children)

            if amountOfChildren > 0:
                self.archive.addToArchive(self.board.changeable, child)

            self.board.changeable = child

        self.pathSolution()
        
        return visited

    def pathSolution(self, solutionState, gameType):
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

            for i in range(len(path)):
                self.board.visualize(path[i], self.colors, gameType, self.game, i)

