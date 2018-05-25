from classes.Board import Board
from copy import copy, deepcopy
import time

class DFS:
    def __init__(self, board, archive):
        """ Takes all information of the board with it's state as the beginning of the game.

        Args:
            board (class): Containing all information of the game.
            archive (class): Containing the archive class.
            endpoint (class): Containing the endpoint class.
        """
        self.board = board

        self.archive = archive
        self.archive.visitedStates[str(self.board.changeable)] = ["beginning!",1]


    def dfs(self, save, maxDepth, popAtMaxDepth):
        """ Runs a depth-first-search on the initialized board.
            The algorithm stops when it finds a solution e.g. a state
            which the red car can move to the end, afterwards it saves the path to a csv file.

        Args:
            save (class): Containing the save class.e
            maxDepth (int): Containing the max depth you want to search to
            popAtMaxDepth (int): Containing how much you would like to pop from the stack  when max depth is reached
        """

        self.save = save
        self.maxDepth = maxDepth
        self.popAtMaxDepth = popAtMaxDepth
        depth = 0

        stack = [self.board.changeable]

        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Running algorithm...\n")

        while self.board.checkSolution() != 0:

            children = self.board.createChildren()

            childLevel = self.archive.visitedStates[str(self.board.changeable)][1] + 1
            depth = childLevel

            amountOfChildren = len(children)

            childrenAvailable = False

            for child in children:
                if str(child) not in self.archive.visitedStates.keys():
                    stack.append(child)
                    self.archive.addToDfsArchive(self.board.changeable, childLevel, child)
                    childrenAvailable = True
                    break
                else:
                    priorKeyLevel = self.archive.visitedStates[str(child)][1]
                    if childLevel < priorKeyLevel:
                        stack.append(child)
                        self.archive.addToDfsArchive(self.board.changeable, childLevel, child)
                        childrenAvailable = True
                        break
                    else:
                        continue

            if childrenAvailable == False:
                stack.pop()

            if depth > self.maxDepth:
                for i in range(0,popAtMaxDepth):
                    stack.pop()

            self.board.changeable = stack[-1]

        self.save.pathSolution(self.board.changeable, "DFS", dfs=True)
        self.save.saveSolution(self.board.changeable, "DFS")

        print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.\n")
