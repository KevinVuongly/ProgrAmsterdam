from queue import Queue, PriorityQueue

class Archive:

    def __init__(self, board, heuristic):
        self.visitedStates = {}

        self.board = board
        self.heuristic = heuristic

    def removeRedundantChild(self, children, childPos, childrenLeft):
        """
        Removes duplicate state e.g. child that is already listed in the archive
        """
        if str(children[childPos]) in self.visitedStates.keys():
            children.pop(childPos)
            childrenLeft -= 1
        else:
            childPos += 1

        return children, childPos, childrenLeft

    def addToArchive(self, parent, childrenOfState):
        """
        Add's child as key, with the parent as the value to the archive dictionary.
        """

        for i in range(len(childrenOfState)):
            self.visitedStates[str(childrenOfState[i])] = parent

    def addToDfsArchive(self, parent, level, child):
        self.visitedStates[str(child)] = [parent, level]

    def addChildBFS(self, queue, childrenOfState):
        """ Puts the child into the queue. """

        for i in range(len(childrenOfState)):
            queue.put(childrenOfState[i])

    def addChildBFSheuristic(self, prioQueue, childrenOfState, level):
        """ Puts the child into the priority queue according to the heuristic score.

        This uses the blockingRedCar heuristic.
        """

        for i in range(len(childrenOfState)):
            blocks = self.heuristic.blockingRedCar(childrenOfState[i])
            prioQueue.put((level + blocks, childrenOfState[i]))

    def addChildBeamSearch(self, n, prioQueue, childrenOfState, solution):
        """ Puts the child into the priority queue according to the heuristic score.

        This uses the positionScore heuristic.
        """

        for i in range(len(childrenOfState)):
            score = self.heuristic.positionScore(n, childrenOfState[i], solution)
            prioQueue.put((score, childrenOfState[i]))

    def addChildAStar(self, n, level, weightMove, prioQueue, childrenOfState, solution):
        """ Puts the child into the priority queue according to the heuristic score.

        This uses the positionScore heuristic and the amount of steps made to get to the given state.
        """

        for i in range(len(childrenOfState)):
            heuristicScore = self.heuristic.positionScore(n, childrenOfState[i], solution)

            prioQueue.put((level * weightMove + heuristicScore, [level, childrenOfState[i], self.board.changeable]))

    def polynomial(self):
        while True:
        	n = input("What degree do you want the polynomial heuristic be?: ")
        	try:
        		n = float(n)
        	except:
        		print("Please give a float.")

        	if isinstance(n, float):
        		break

        return n

    def addChildDFS(self, parent, stack, childrenOfState):
        """
        Add's child as key, with the parent as the value to the archive dictionary.
        """

        for i in range(len(childrenOfState)):
            if i not in self.visitedStates.keys():
                stack.append(childrenOfState[i])
                self.visitedStates[str(childrenOfState[i])] = parent
                break
            stack.pop()

        return stack

    def manipulateChildren(self, algorithm=0):
        """ Creates a list of all possible children of a state. If a child is already in the archive,
            removes it from the list. If not, add it to the archive.
        """
        children = self.board.createChildren()

        amountOfChildren = len(children)
        childToCheck = 0

        while childToCheck != amountOfChildren:
            children, childToCheck, amountOfChildren = self.removeRedundantChild(children, childToCheck, amountOfChildren)

        return children, amountOfChildren
