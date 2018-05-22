
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



    def semiRandomSelection(self, save):
        """
        Looks for all moves possible and randomly choses a state that he hasn't visited each time,
        until solved. If al possible moves are visited states, it goes back one move.
        """
        self.save = save
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

        self.save.getPath(self.board.changeable, foldername)
        self.save.saveSolution(self.board.changeable, foldername)
