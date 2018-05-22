from classes.Heuristics import Heuristic
from queue import Queue, PriorityQueue

class Archive:

    def __init__(self, heuristic):
        self.visitedStates = {}
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
        for i in range(len(childrenOfState)):
            self.visitedStates[str(childrenOfState[i])] = parent

    def addToDfsArchive(self, parent, level, child):
        self.visitedStates[str(child)] = [parent, level]

    def addChildBFS(self, queue, childrenOfState):
        """
        Add's child as key, with the parent as the value to the archive dictionary.
        """

        for i in range(len(childrenOfState)):
            queue.put(childrenOfState[i])

    def addChildBFSheuristic(self, prioQueue, childrenOfState, level):

        for i in range(len(childrenOfState)):
            blocks = self.heuristic.blockingRedCar(childrenOfState[i])
            prioQueue.put((level + blocks, childrenOfState[i]))

    def addChildBeamSearch(self, prioQueue, childrenOfState, solution):

        for i in range(len(childrenOfState)):
            score = self.heuristic.positionScore(childrenOfState[i], solution)
            prioQueue.put((score, childrenOfState[i]))

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
