from queue import Queue, PriorityQueue

class Archive:
    """A class that contains all actions concerning the dictionary, which is the archive. """

    def __init__(self, board, heuristic):
        """ Initialization of the archive's parameters.

        Initialization:
            self.visitedStates: Initialize the archive.

        Args:
            board (class): Containing all information of the game.
            heuristic (class): Containing all information of the used heuristics
        """
        self.visitedStates = {}

        self.board = board
        self.heuristic = heuristic

    def removeRedundantChild(self, children, childPos, childrenLeft):
        """ Removes duplicate state e.g. child that is already listed in the archive

        Args and returns:
            children (list of lists): All children of the current state checked for.
            childPos (int): The position of a child inside children.
            childrenLeft (int): Amount of children left in the childen list.
        """

        if str(children[childPos]) in self.visitedStates.keys():
            children.pop(childPos)
            childrenLeft -= 1
        else:
            childPos += 1

        return children, childPos, childrenLeft

    def addToArchive(self, parent, childrenOfState):
        """ Add's child as key, with the parent as the value to the archive dictionary.

        Args:
            parent (list): The parent of the children.
            childrenOfState(list of lists): All children of the parent.
        """

        for i in range(len(childrenOfState)):
            self.visitedStates[str(childrenOfState[i])] = parent

    def addToDfsArchive(self, parent, level, child):
        """ Add's child as key, with the parent and the depth as the value to the archive dictionary.

        Args:
            parent (list): The parent of the child.
            level (int): The depth e.g. the amount of moves made to get to the current child.
            child (list): The child of the parent.
        """
        self.visitedStates[str(child)] = [parent, level]

    def addChildBFS(self, queue, childrenOfState):
        """ Puts the child into the queue.

        Args:
            queue (queue.Queue): The current queue that needs to be updated
            childrenOfState (list): List of children that needs to put into the queue.
        """

        for i in range(len(childrenOfState)):
            queue.put(childrenOfState[i])

    def addChildBFSheuristic(self, prioQueue, childrenOfState, level):
        """ Puts the child into the priority queue according to the heuristic score.
            This uses the blockingRedCar heuristic.

        Args:
            prioQueue (queue.PriorityQueue): The current priority queue that needs to be updated.
            childrenOfState (list of lists): List of children that needs to put into the queue.
            level (int): The depth e.g. the amount of moves made to get to the current child.

        Initialization:
            blocks (int): Number of cars blocking the way of the red car.
        """

        for i in range(len(childrenOfState)):
            blocks = self.heuristic.blockingRedCar(childrenOfState[i])
            prioQueue.put((level + blocks, childrenOfState[i]))

    def addChildBeamSearch(self, prioQueue, childrenOfState, solution):
        """ Puts the child into the priority queue according to the heuristic score.
            This uses the positionScore heuristic.

        Args:
            prioQueue (queue.PriorityQueue): The current priority queue that needs to be updated.
            childrenOfState (list of lists): List of children that needs to put into the queue.
            solution (list): The endpoint e.g. solution state of the game.
                             Needed to calculate the score.
        """

        for i in range(len(childrenOfState)):
            score = self.heuristic.positionScore(childrenOfState[i], solution)
            prioQueue.put((score, childrenOfState[i]))

    def addChildAStar(self, level, prioQueue, childrenOfState, solution):
        """ Puts the level, child and parent accordingly into the priority queue
            according to the heuristic score.
            This uses the positionScore heuristic and the amount of steps made to get
            to the given state.

        Args:
            level (int): The depth e.g. the amount of moves made to get to the current child.
            prioQueue (queue.PriorityQueue): The current priority queue that needs to be updated.
            childrenOfState (list of lists): List of children that needs to put into the queue.
            solution (list): The endpoint e.g. solution state of the game.
                             Needed to calculate the score.
        """

        for i in range(len(childrenOfState)):
            heuristicScore = self.heuristic.positionScore(childrenOfState[i], solution, True)

            prioQueue.put((level + heuristicScore, [level, childrenOfState[i], self.board.changeable]))

    def manipulateChildren(self):
        """ Creates a list of all possible children of a state using createChildren().
            If a child is already in the archive, removes it from the list. If not, add it to the archive.
            Uses removeRedundantChild() for this action.

        Return:
            children (list of lists): The newly updated children that hasn't been checked for yet.
            amountOfChildren (int): The amount of children.
        """
        children = self.board.createChildren()

        amountOfChildren = len(children)
        childToCheck = 0

        while childToCheck != amountOfChildren:
            children, childToCheck, amountOfChildren = self.removeRedundantChild(children, childToCheck, amountOfChildren)

        return children, amountOfChildren
