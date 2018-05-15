from classes.Board import Board
from copy import copy, deepcopy

class BFS:
        def __init__(self, game, board, archive, colors):
            """
            Takes all information of the board with it's state as the beginning of the game.
            """
            self.game = game
            self.board = board

            self.archive = archive
            self.archive.visitedStates[str(self.board.changeable)] = "beginning!"

            self.colors = colors

        def bfs(self):
            """
            Runs breadth first search on the initialized board. The algorithm stops when
            it finds a solution e.g. a state which the red car can move to the end.
            """

            queue = [self.board.changeable]

            while self.board.checkSolution() != 0:

                children = self.board.createChildren()

                amountOfChildren = len(children)
                childToCheck = 0

                while childToCheck != amountOfChildren:
                    children, childToCheck, amountOfChildren = self.archive.removeRedundantChild(children, childToCheck, amountOfChildren)

                if amountOfChildren > 0:
                    self.archive.addChildBFS(self.board.changeable, queue, children)

                queue.pop(0)
                self.board.changeable = queue[0]

            self.pathSolution(self.board.changeable, "BFS")

        def bfsHeuristic(self):
            """
            Runs breadth first search on the initialized board. The algorithm stops when
            it finds a solution e.g. a state which the red car can move to the end.

            Only now the queue is using a heuristic instead of first come first serve.
            """
            redCarSize = 2

            blocksPossible = self.board.gridSize - redCarSize + 1
            queue = [[] for i in range(blocksPossible)]

            blocksState = self.board.blockingCars(self.board.changeable)
            queue[blocksState].append(self.board.changeable)

            visited = 100000

            while self.board.checkSolution() != 0:

                children = self.board.createChildren()

                if len(self.archive.visitedStates) > visited:
                    print(len(self.archive.visitedStates))
                    visited += 100000

                amountOfChildren = len(children)
                childToCheck = 0

                while childToCheck != amountOfChildren:
                    children, childToCheck, amountOfChildren = self.archive.removeRedundantChild(children, childToCheck, amountOfChildren)

                if amountOfChildren > 0:
                    for i in range(amountOfChildren):
                        blocks = self.board.blockingCars(children[i])

                        if len(queue[blocks]) < 50000:
                            queue[blocks].append(children[i])

                        self.archive.visitedStates[str(children[i])] = self.board.changeable

                blocksState = self.board.blockingCars(self.board.changeable)

                queue[blocksState].pop(0)

                for i in range(blocksPossible):
                    if len(queue[i]) > 0:
                        self.board.changeable = queue[i][0]
                        break

            self.pathSolution(self.board.changeable, "BFSheuristic")

        def pathSolution(self, solutionState, gameType):
            """
            Visualizes the path found through breadth first search.
            """
            path = [solutionState]

            child = solutionState
            parent = self.archive.visitedStates[str(solutionState)]

            while self.archive.visitedStates[str(child)] != "beginning!":
                path.insert(0, parent)

                child = parent
                parent = self.archive.visitedStates[str(child)]

            for i in range(len(path)):
                self.board.visualize(path[i], self.colors, gameType, self.game, i)
