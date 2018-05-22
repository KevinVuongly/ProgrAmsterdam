import ast
import time
from copy import copy
from queue import Queue, PriorityQueue

class BFS:
    def __init__(self, board, archive):
        """ Takes all information of the board with it's state as the beginning of the game. """
        self.board = board

        self.archive = archive
        self.archive.visitedStates[str(self.board.changeable)] = "beginning!"

    def bfs(self, type, save):
        """ Runs breadth first search on the initialized board.

        The algorithm stops when it finds a solution e.g. a state which the red car can move to the end.

        if type = normal:
            Runs breadth first search.
        if type = heuristic:
            Runs breadth first search with blocking red car heuristic. Checks the amount of cars
            blocking the way of the red car. Also keeps track of the level e.g. the amount of steps
            it took to get to the given board state.
        if type = beamsearch:
            Uses breadth first search "beam search" according to the "positionScore" heuristic
            in the heuristic class. See Heuristics.py for more information about the used heuristic.
        """

        self.type = type
        self.save = save

        queue, standbyQueue = self.initQueue()

        while self.board.checkSolution() != 0 and self.everythingExplored == False:
            children, amountOfChildren = self.archive.manipulateChildren()

            if amountOfChildren > 0:
                self.archive.addToArchive(self.board.changeable, children)

            if type == "normal":
                self.archive.addChildBFS(queue, children)
            elif type == "heuristic":
                self.archive.addChildBFSheuristic(standbyQueue, children, self.level)
            elif type == "beamsearch":
                self.archive.addChildBeamSearch(standbyQueue, children, self.solution)

            if not queue.empty():
                self.board.changeable = queue.get()
            else:
                self.everythingExplored = True

            if self.board.changeable == self.level:
                self.level += 1

                self.activateQueue(type, queue, standbyQueue)

        self.finishedAlgorithm()

        return self.board.changeable

    def initQueue(self):
        """ Initialize the queue for the provided algorithm. """
        self.level = 0
        self.everythingExplored = False

        activeQueue = Queue()
        activeQueue.put(self.board.changeable)

        inactiveQueue = None

        if self.type == "heuristic" or self.type == "beamsearch":
            activeQueue.put(self.level)

            inactiveQueue = PriorityQueue()

            if self.type == "beamsearch":
                self.width, self.solution = self.beamSearchInput()

        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Running algorithm...")

        return activeQueue, inactiveQueue

    def beamSearchInput(self):
        """ Get the input needed for the beam search to run. """
        while True:

            width = input("What's the width you want to use for the beamsearch?: ")

            try:
            	width = int(width)
            except:
            	print("Please pick a feasible width.")

            if isinstance(width, int):

            	if width < 0:
            		print("Please pick a feasible width.")
            	else:
            		break

        solution = input("Paste your solution state: ")
        solution = ast.literal_eval(solution)

        return width, solution

    def activateQueue(self, typeAlgo, activeQueue, inactiveQueue):
        """ When the queue is empty, put the priorityQueue into the active queue. """

        if typeAlgo == "beamsearch":
            if self.width > inactiveQueue.qsize():
                nonPrunedNodes = inactiveQueue.qsize()
            else:
                nonPrunedNodes = copy(self.width)

        elif typeAlgo == "heuristic":
            nonPrunedNodes = inactiveQueue.qsize()

        for i in range(nonPrunedNodes):
            activeQueue.put(list(inactiveQueue.get()[1]))

        activeQueue.put(self.level)

        self.board.changeable = activeQueue.get()
        inactiveQueue = PriorityQueue()

    def finishedAlgorithm(self):
        """
        When the algorithm is finished, save the path if the solution is found.
        If not, nothing happens.
        """

        if self.board.checkSolution() == 0:
            if self.type == "normal":
                foldername = "BFS"
            elif self.type == "heuristic":
                foldername = "BFSHeuristic"
            elif self.type == "beamsearch":
                foldername = "BFSBeamSearch"

            self.save.pathSolution(self.board.changeable, foldername)

            print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.")

        else:
            print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution not found.")
