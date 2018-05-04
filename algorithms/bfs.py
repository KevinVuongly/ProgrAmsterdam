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

            stack = [self.board.changeable]

            self.archive = {}
            self.archive[str(self.board.changeable)] = "beginning!"

            iterations = 0

            while self.board.checkSolution() != 0:

                children = self.board.createChildren()

                amountOfChildren = len(children)
                childToCheck = 0

                while childToCheck != amountOfChildren:
                    if str(children[childToCheck]) in self.archive.keys():
                        children.pop(childToCheck)
                        amountOfChildren -= 1
                    else:
                        childToCheck += 1

                if len(children) > 0:
                    for i in range(len(children)):
                        stack.append(children[i])
                        self.archive[str(children[i])] = self.board.changeable

                stack.pop(0)
                self.board.changeable = stack[0]

            self.pathSolution(self.board.changeable)

            print("WE HAVE FOUND IT!")

        def pathSolution(self, solutionState):
            path = [solutionState]

            child = solutionState
            parent = self.archive[str(solutionState)]

            while self.archive[str(child)] != "beginning!":
                path.insert(0, parent)

                child = parent
                parent = self.archive[str(child)]

            for i in range(len(path)):
                self.board.visualize(path[i], self.colors, "BFS", self.game, i)
