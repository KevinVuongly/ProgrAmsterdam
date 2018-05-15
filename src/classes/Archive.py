class Archive:

    def __init__(self):
        self.visitedStates = {}

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

    def addChildBFS(self, parent, queue, childrenOfState):
        """
        Add's child as key, with the parent as the value to the archive dictionary.
        """

        for i in range(len(childrenOfState)):
            queue.append(childrenOfState[i])
            self.visitedStates[str(childrenOfState[i])] = parent

        return queue
