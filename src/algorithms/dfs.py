from classes.Board import Board
from copy import copy, deepcopy

class DFS:
        def __init__(self, game, board, archive, colors):
            """
            Takes all information of the board with it's state as the beginning of the game.
            """
            self.game = game
            self.board = board

            self.archive = archive
            self.archive.visitedStates[str(self.board.changeable)] = ["beginning!",1]

            self.colors = colors

        def dfs(self):
            """
            Runs depth first search on the initialized board. The algorithm stops when
            it finds a solution e.g. a state which the red car can move to the end.
            """

            maxDepth = 300
            depth = 0

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

                if depth > maxDepth:
                    for i in range(0,200):
                        stack.pop()

                self.board.changeable = stack[-1]


                """


                while childToCheck != amountOfChildren:
                    children, childToCheck, amountOfChildren = self.archive.removeRedundantChild(children, childToCheck, amountOfChildren)

                if amountOfChildren > 0:
                    self.archive.addChildDFS(self.board.changeable, stack, children)
                else:
                    stack.pop()

                depth += 1
                
                
                if depth >= maxDepth:
                    for i in range(0,10):
                        stack.pop    
                    depth -= 10
                """



            self.pathSolution(self.board.changeable, "DFS")



        def pathSolution(self, solutionState, gameType):
            """
            Visualizes the path found through breadth first search.
            """
            path = [solutionState]

            child = copy(solutionState)

            parent = self.archive.visitedStates[str(solutionState)][0]

            while self.archive.visitedStates[str(child)][0] != "beginning!":
                path.insert(0, parent)

                child = parent
                parent = self.archive.visitedStates[str(child)][0]

            for i in range(len(path)):
                self.board.visualize(path[i], self.colors, gameType, self.game, i)


            return len(path)