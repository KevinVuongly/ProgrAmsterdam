from classes.Board import Board
from classes.Heuristics import Heuristic
import ast
import time
from copy import copy, deepcopy
from queue import Queue, PriorityQueue

class BFSBetweenStates:
    def __init__(self, board, archive, endState):
        """
        Takes all information of the board with it's state as the beginning of the game.
        """
        self.game = game
        self.board = board

        self.archive = archive
        self.archive.visitedStates[str(self.board.changeable)] = "beginning!"

        self.endState = endState

    def bfsBetweenStates(self, save):
        """
        Runs breadth first search on the initialized board. The algorithm stops when
        it finds a solution e.g. a state which the red car can move to the end.
        """

        self.save = save
        foldername = "betweenStates"

        queue = Queue()
        queue.put(self.board.changeable)

        while self.board.changeable != self.endState:

            children = self.board.createChildren()

            amountOfChildren = len(children)
            childToCheck = 0

            while childToCheck != amountOfChildren:
                children, childToCheck, amountOfChildren = self.archive.removeRedundantChild(children, childToCheck, amountOfChildren)

            if amountOfChildren > 0:
                self.archive.addToArchive(self.board.changeable, children)
                self.archive.addChildBFS(self.board.changeable, queue, children)

            self.board.changeable = queue.get()

        self.save.getPath(self.board.changeable, foldername)
        self.save.saveSolution(self.board.changeable, foldername)
