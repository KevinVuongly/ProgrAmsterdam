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

    def addChildBFS(self, parent, queue, childrenOfState):
        """
        Add's child as key, with the parent as the value to the archive dictionary.
        """

        for i in range(len(childrenOfState)):
            queue.put(childrenOfState[i])

        return queue

    def addChildBeamSearch(self, width, parent, queue, childrenOfState, solution):

        childrenScore = PriorityQueue()

        for i in range(len(childrenOfState)):
            score = self.heuristic.positionScore(childrenOfState[i], solution)
            childrenScore.put((score, childrenOfState[i]))

        if width > len(childrenOfState):
            width = len(childrenOfState)

        for i in range(width):
            queue.put(list(childrenScore.get()[1]))

        return queue


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