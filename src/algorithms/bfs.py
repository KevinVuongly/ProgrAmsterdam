from classes.Board import Board
from classes.Heuristics import Heuristic
import ast
import time
from copy import copy, deepcopy
from queue import Queue, PriorityQueue

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

        def bfs(self, heuristic=0):
            """
            Runs breadth first search on the initialized board. The algorithm stops when
            it finds a solution e.g. a state which the red car can move to the end.
            """

            self.heuristic = heuristic

            queue = Queue()
            queue.put(self.board.changeable)

            while self.board.checkSolution() != 0:

                children = self.board.createChildren()

                amountOfChildren = len(children)
                childToCheck = 0

                while childToCheck != amountOfChildren:
                    children, childToCheck, amountOfChildren = self.archive.removeRedundantChild(children, childToCheck, amountOfChildren)

                if amountOfChildren > 0:
                    self.archive.addToArchive(self.board.changeable, children)
                    self.archive.addChildBFS(self.board.changeable, queue, children)

                self.board.changeable = queue.get()

            self.pathSolution(self.board.changeable, "BFS")

            print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.")

            return self.board.changeable

        def blockingRedCarHeuristic(self, heuristic):
            """
            Runs breadth first search on the initialized board. The algorithm stops when
            it finds a solution e.g. a state which the red car can move to the end.

            Only now the queue is using a heuristic instead of first come first serve.
            """
            self.heuristic = heuristic

            redCarSize = 2

            blocksPossible = self.board.gridSize - redCarSize + 1
            queue = [Queue() for i in range(blocksPossible)]

            blocksState = self.heuristic.blockingRedCar(self.board.changeable)
            queue[blocksState].put(self.board.changeable)

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
                        blocks = self.heuristic.blockingRedCar(children[i])
                        queue[blocks].put(children[i])

                        self.archive.visitedStates[str(children[i])] = self.board.changeable

                blocksState = self.heuristic.blockingRedCar(self.board.changeable)

                for i in range(blocksPossible):
                    if queue[i].qsize() > 0:
                        self.board.changeable = queue[i].get()
                        break

            self.pathSolution(self.board.changeable, "BFSheuristic")

            print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.")

            return self.board.changeable

        def beamSearch(self, width):
            """
            Runs BFS with beam search. Only adds the best x states according to our heuristic to the queue.
            Other states get's pruned.
            """

            solution = input("Paste your solution state: ")
            solution = ast.literal_eval(solution)

            queue = Queue()
            queue.put(self.board.changeable)

            level = 0

            while self.board.checkSolution() != 0 and queue.qsize() > 0:
                children = self.board.createChildren()

                amountOfChildren = len(children)
                childToCheck = 0

                while childToCheck != amountOfChildren:
                    children, childToCheck, amountOfChildren = self.archive.removeRedundantChild(children, childToCheck, amountOfChildren)

                if amountOfChildren > 0:
                    self.archive.addToArchive(self.board.changeable, children)
                    self.archive.addChildBeamSearch(self.board.changeable, queue, children, solution, level)

                self.board.changeable = queue.get()
                
                if self.board.changeable = "end":
                    self.board.changeable = queue.get()

            if self.board.checkSolution() == 0:
                self.pathSolution(self.board.changeable, "BFSBeamSearch")
                print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.")

            else:
                print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution not found.")

            return self.board.changeable

        def pathSolution(self, solutionState, gameType):
            """
            Visualizes the path found through breadth first search.
            """
            path = [solutionState]

            child = copy(solutionState)

            parent = self.archive.visitedStates[str(child)]

            while self.archive.visitedStates[str(child)] != "beginning!":
                path.insert(0, parent)

                child = parent
                parent = self.archive.visitedStates[str(child)]

            for i in range(len(path)):
                self.board.visualize(path[i], self.colors, gameType, self.game, i)
