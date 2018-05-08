from classes.Board import Board
from copy import copy, deepcopy

class BFS:
        def __init__(self, game, board, archive, colors):
            """
            Takes all information of the board with it's state as the beginning of the game.
            """
            self.game = game
            self.board = board
            self.archive = archive
            self.colors = colors

        def bfs(self):
            """
            Runs breadth first search on the initialized board. The algorithm stops when
            it finds a solution e.g. a state which the red car can move to the end.
            """

            queue = [self.board.changeable]

            self.archive.visitedStates[str(self.board.changeable)] = "beginning!"

            while self.board.checkSolution() != 0:

                children = self.board.createChildren()

                amountOfChildren = len(children)
                childToCheck = 0

                while childToCheck != amountOfChildren:
                    children, childToCheck, amountOfChildren = self.archive.removeRedundantChild(children, childToCheck, amountOfChildren)

                if amountOfChildren > 0:
                    self.archive.addChild(self.board.changeable, queue, children)

                queue.pop(0)
                self.board.changeable = queue[0]

            self.pathSolution(self.board.changeable)

        def pathSolution(self, solutionState):
            """
            Visualizes the path found through breadth first search.
            """
            path = [solutionState]

            child = solutionState
            parent = self.archive.visitedStates[str(solutionState)]

            while self.archive.visitedStates[str(child)] != "beginning!":
                path.insert(0, parent)

                child = parent
                parent = self.archive.visitedStates[str(child)]

            for i in range(len(path)):
                self.board.visualize(path[i], self.colors, "BFS", self.game, i)
