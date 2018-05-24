from classes.Board import Board
from classes.Save import Save
from copy import copy, deepcopy
import time
import random

class Random:
    def __init__(self, board, archive, save):
        """
        Takes all information of the board with it's state as the beginning of the game.
        """
        self.board = board
        self.archive = archive
        self.save = save
        self.archive.visitedStates[str(self.board.changeable)] = "beginning!"

    def semiRandomSelection(self):
        """
        Looks for all moves possible and randomly choses a state that he hasn't visited each time,
        until solved. If al possible moves are visited states, it goes back one move.
        """

        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Running algorithm...")

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

        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.")

        return self.board.changeable
