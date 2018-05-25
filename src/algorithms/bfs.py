import time
from copy import copy
from queue import Queue, PriorityQueue

class BFS:
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
        self.archive.visitedStates[str(self.board.changeable)] = "beginning!"

        self.endpoint = endpoint
        self.save = save

    def bfs(self, type):
        """ Runs breadth first search on the initialized board.
            The algorithm stops when it finds a solution e.g. a state which the red car can
            move to the end.

        Arg:
            if type = normal:
                Runs breadth first search.
            if type = heuristic:
                Runs breadth first search with blocking red car heuristic. Checks the amount of cars
                blocking the way of the red car. Also keeps track of the level e.g. the amount of steps
                it took to get to the given board state.
            if type = beamsearch:
                Uses breadth first search "beam search" according to the "positionScore" heuristic
                in the heuristic class. See Heuristics.py for more information about the used heuristic.

        Return:
            The last state e.g. the last move of the solution.
        """

        self.type = type

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
        """ Initialize the queue(s) for the provided algorithm.

        Initializations:
            self.level: Start at depth level 0.
            self.everythingExplored: The whole stateSpace hasn't been explored yet. Start as False.
                                     This might happen when the beamwidth is marginally small.

        Return:
            activeQueue: The queue that will be used for the algorithm.
            inactiveQueue: The queue that will be put in the activeQueue when the activeQueue is empty.
                           Will only be used for the heuristic and the beamsearch algorithms.
        """
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

        self.endpoint = None

        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Running algorithm...\n")

        return activeQueue, inactiveQueue

    def beamSearchInput(self):
        """ Get the input needed for the beam search to run.

        Input:
            width: The width you want to use for your beamsearch. Must be a positive integer.

        Return:
            width: See above.
            solutionState: Will contain the endpoint. If the endpoint doesn't exist yet,
                           it will create a new endpoint through the random algorithm.
        """
        while True:

            width = input("What's the width you want to use for the beamsearch?: ")

            try:
            	width = int(width)
            except:
            	print("Please pick a feasible width.\n")

            if isinstance(width, int):

            	if width < 0:
            		print("Please pick a feasible width.\n")
            	else:
            		break

        solutionState = self.endpoint.findEndPoint()

        return width, solutionState

    def activateQueue(self, typeAlgo, activeQueue, inactiveQueue):
        """ When the queue is empty, put the priorityQueue into the active queue.
            If it's a beamsearch, it makes sure it stays within the beamwidth.

        Args:
            typeAlgo (string): The type of algorithm that is currently used.
            activeQueue (queue.Queue): The queue that is currently empty.
            inactiveQueue (queue.PriorityQueue): Inactive queue. Will be put in the active queue,
                                                 afterwards made empty again.
        """

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
        """ When the algorithm is finished, save the path if the solution is found.
            If not, nothing happens.
        """

        if self.board.checkSolution() == 0:
            if self.type == "normal":
                folderName = "BFS"
            elif self.type == "heuristic":
                folderName = "BFSHeuristic"
            elif self.type == "beamsearch":
                folderName = "BFSBeamSearch"

            self.save.pathSolution(self.board.changeable, folderName)
            self.save.saveSolution(self.board.changeable, folderName)

            print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.\n")

        else:
            print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution not found. Please retry.\n")
