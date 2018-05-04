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
            print("Test")
