import ast
import time
from copy import copy
from queue import Queue, PriorityQueue

class Astar:
    def __init__(self, board, archive):
        """
        Takes all information of the board with it's state as the beginning of the game.
        """
        self.board = board

        self.archive = archive

        self.parent = "beginning!"

    def astar(self, save):
        """ Runs A*-search on the initialized board.

        The algorithm stops when it finds a solution e.g. a state which the red car can move to the end.
        """

        self.save = save

        weight, n, solution = self.initAStar()
        currentScore = 0

        depth = 0

        queue = PriorityQueue()

        while self.board.changeable != solution:
            if str(self.board.changeable) not in self.archive.visitedStates.keys() or currentScore < self.archive.visitedStates[str(self.board.changeable)][0]:
                self.archive.visitedStates[str(self.board.changeable)] = [currentScore, self.parent]

                children, amountOfChildren = self.archive.manipulateChildren()

                self.archive.addChildAStar(n, depth + 1, weight, queue, children, solution)

            [currentScore, [depth, self.board.changeable, self.parent]] = list(queue.get())

        self.archive.visitedStates[str(self.board.changeable)] = [currentScore, self.parent]

        self.save.pathSolution(self.board.changeable, "AStar", True)

        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.")

        return self.board.changeable

    def initAStar(self):
        """ Asks for parameters needed for the algorithm to start."""
        while True:
            weightOfMove = input("How heavy do you want the move to count in the score? (Scale between [0, inf): ")

            try:
                weightOfMove = float(weightOfMove)
            except:
                print("Please pick a number within the given range")

            if isinstance(weightOfMove, float):
                if weightOfMove < 0:
                    print("Please pick a number within the given range.")
                else:
                    break

        n = self.archive.polynomial()

        solutionState = input("Paste your solution state: ")
        solutionState = ast.literal_eval(solutionState)

        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Running algorithm...")

        return weightOfMove, n, solutionState
