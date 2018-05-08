from classes.Board import Board
from copy import copy, deepcopy

class BFS:
        def __init__(self, game, board, colors):
            """
            Takes all information of the board with it's state as the beginning of the game.
            """
            self.game = game
            self.board = board
            self.colors = colors

        def bfs(self):
            """
            Runs breadth first search on the initialized board. The algorithm stops when
            it finds a solution e.g. a state which the red car can move to the end.
            """

            self.queue = [self.board.changeable]

            self.archive = {}
            self.archive[str(self.board.changeable)] = "beginning!"

            while self.board.checkSolution() != 0:

                children = self.board.createChildren()

                amountOfChildren = len(children)
                childToCheck = 0

                while childToCheck != amountOfChildren:
                    children, childToCheck, amountOfChildren = self.removeRedundantChild(children, childToCheck, amountOfChildren)

                if amountOfChildren > 0:
                    self.addToArchive(children)

                self.queue.pop(0)
                self.board.changeable = self.queue[0]

            print(len(self.archive))

            self.pathSolution(self.board.changeable)

        def removeRedundantChild(self, children, childPos, childrenLeft):
            """
            Removes duplicate state e.g. child that is already listed in the archive
            """
            if str(children[childPos]) in self.archive.keys():
                children.pop(childPos)
                childrenLeft -= 1
            else:
                childPos += 1

            return children, childPos, childrenLeft

        def addToArchive(self, childrenOfState):
            """
            Add's child as key, with the parent as the value to the archive dictionary.
            """
            for i in range(len(childrenOfState)):
                self.queue.append(childrenOfState[i])
                self.archive[str(childrenOfState[i])] = self.board.changeable

        def pathSolution(self, solutionState):
            """
            Visualizes the path found through breadth first search.
            """
            path = [solutionState]

            child = solutionState
            parent = self.archive[str(solutionState)]

            while self.archive[str(child)] != "beginning!":
                path.insert(0, parent)

                child = parent
                parent = self.archive[str(child)]

            for i in range(len(path)):
                self.board.visualize(path[i], self.colors, "BFS", self.game, i)
