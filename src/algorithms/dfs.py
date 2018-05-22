from classes.Board import Board
from copy import copy, deepcopy

class DFS:
        def __init__(self, board, archive):
            """
            Takes all information of the board with it's state as the beginning of the game.
            """
            self.board = board

            self.archive = archive
            self.archive.visitedStates[str(self.board.changeable)] = ["beginning!",1]


        def dfs(self, save, maxDepth, popAtMaxDepth):
            """
            Runs depth first search on the initialized board. The algorithm stops when
            it finds a solution e.g. a state which the red car can move to the end.
            """

            self.save = save
            self.maxDepth = maxDepth
            self.popAtMaxDepth = popAtMaxDepth
            depth = 0
            foldername = "DFS"

            stack = [self.board.changeable]

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

            self.save.pathSolutionDfs(self.board.changeable, foldername)
            self.save.saveSolution(self.board.changeable, foldername)






