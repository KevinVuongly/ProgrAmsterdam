from classes.Board import Board
from copy import copy, deepcopy

class BFS:
        def __init__(self, board):
            """
            Takes all information of the board with it's state as the beginning of the game.
            """
            self.board = board

        def bfs(self):
            """
            Runs breadth first search on the initialized board. The algorithm stops when
            it finds a solution e.g. a state which the red car can move to the end.
            """

            iterations = 0

            archive = {}
            archive[0] = self.board.changeable

            while self.board.checkSolution != 0:
                children = self.board.createChildren()

                initialArchiveLength = len(archive)
                amountOfChildren = len(children)

                for i in range(amountOfChildren):
                    for j in range(initialArchiveLength):
                        if archive[j] == children[i]:
                            children.pop(i)
                            break

                for i in range(len(children)):
                    archive[initialArchiveLength + 1 + i] = children[i]

                iterations += 1

                self.board.changeable = archive[iterations]
