from classes.Board import Board
from classes.Heuristics import Heuristic
import ast
import time
from copy import copy, deepcopy
from queue import Queue, PriorityQueue

class BFS:
        def __init__(self, game, board, archive, colors, endState):
            """
            Takes all information of the board with it's state as the beginning of the game.
            """
            self.game = game
            self.board = board

            self.archive = archive
            self.archive.visitedStates[str(self.board.changeable)] = "beginning!"

            self.colors = colors
            self.state = endState 

        def bfs(self, endState):
            """
            Runs breadth first search on the initialized board. The algorithm stops when
            it finds a solution e.g. a state which the red car can move to the end.
            """

            queue = Queue()
            queue.put(self.board.changeable)

            while self.board.changeable != endState:

                children = self.board.createChildren()

                amountOfChildren = len(children)
                childToCheck = 0

                while childToCheck != amountOfChildren:
                    children, childToCheck, amountOfChildren = self.archive.removeRedundantChild(children, childToCheck, amountOfChildren)

                if amountOfChildren > 0:
                    self.archive.addToArchive(self.board.changeable, children)
                    self.archive.addChildBFS(self.board.changeable, queue, children)

                self.board.changeable = queue.get()

            self.pathSolution(self.board.changeable, "BFS")

            #print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.")

            return self.board.changeable

       
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
