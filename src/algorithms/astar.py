from algorithms.random import Random
import time
from copy import copy, deepcopy
from queue import Queue, PriorityQueue

class Astar:
    def __init__(self, board, archive, endpoint, save):
        """ Takes all information of the board with it's state as the beginning of the game.

        Args:
            board (class): Containing all information of the game.
            archive (class): Containing the archive class.
            endpoint (class): Containing the endpoint class.
            save (class): Containing the save class.
        """
        self.board = board
        self.archive = archive
        self.endpoint = endpoint
        self.save = save

        self.parent = "beginning!"

    def astar(self):
        """ Runs A*-search on the initialized board.
            The algorithm stops when it finds a solution e.g. a state
            which the red car can move to the end, afterwards it visualizes the solution.

        Return:
            The last state e.g. the last move of the solution.
        """

        solution = self.initAStar()
        currentScore = 0

        depth = 0

        queue = PriorityQueue()

        while self.board.changeable != solution:
            if str(self.board.changeable) not in self.archive.visitedStates.keys() or currentScore < self.archive.visitedStates[str(self.board.changeable)][0]:
                self.archive.visitedStates[str(self.board.changeable)] = [currentScore, self.parent]

                children, amountOfChildren = self.archive.manipulateChildren()

                self.archive.addChildAStar(depth + 1, queue, children, solution)

            [currentScore, [depth, self.board.changeable, self.parent]] = list(queue.get())

        # Put the last move in the archive. Needed to create the path.
        self.archive.visitedStates[str(self.board.changeable)] = [currentScore, self.parent]

        self.save.pathSolution(self.board.changeable, "AStar", astar=True)
        self.save.saveSolution(self.board.changeable, "AStar")

        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.\n")

        return self.board.changeable

    def initAStar(self):
        """ Asks for the endpoint needed for the algorithm to start.

        Parameter:
            solutionState(list): Will contain the endpoint. If the endpoint doesn't exist yet,
                                 it will create a new endpoint through the random algorithm.
        """

        solutionState = self.endpoint.findEndPoint()

        self.endpoint = None

        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Running algorithm...\n")

        return solutionState
