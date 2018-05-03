from classes.Board import Board
import copy
import random

class Bfs:
    def __init__(self, board):
        """
        """
        self.board = board


    def randomSelection(self):
        """ Looks for all moves possible and randomly choses one until solved """
        counter = 0
        child = []
        while self.board.checkSolution != 0:
            counter += 1
            children = []
            j = 0
            posMoves = self.board.checkPossibleMoves()
            print(counter)
            for i in range(self.board.nrOfCars):
                for move in posMoves[i]:
                    if not move:
                        continue
                    else:
                        child = copy.deepcopy(self.board.changeable)
                        child[i] = child[i] + posMoves[i][j]
                        children.append(child)
                    j += 1
                j = 0
            if not children:
                continue
            else:
                self.board.changeable = random.choice(children)
        return self.board

    def semiRandomSelection(self):
        """
        Looks for all moves possible and randomly choses one until solved, without
        back to board configurations visited before. If it can't find a move to 
        go to a board configuarion that it has been before it goes to a random visited 
        (Later added if a configuration has no non-visited options, skip that one. 
            i hoped the code would find a solution faster )
        """
        beginState = copy.deepcopy(self.board.changeable)
        counter = 0
        child = []
        visited = []
        noOptions = []
        while self.board.checkSolution != 0:
            counter += 1
            children = []
            j = 0
            posMoves = self.board.checkPossibleMoves()
            print(counter)
            for i in range(self.board.nrOfCars):
                for move in posMoves[i]:
                    if not move:
                        continue
                    else:
                        child = copy.deepcopy(self.board.changeable)
                        child[i] = child[i] + posMoves[i][j]
                        children.append(child)
                    j += 1
                j = 0
            if not children:
                continue
            else:
                self.board.changeable = random.choice(children)
                j = 0
                if self.board.changeable not in visited:
                    visited.append(self.board.changeable)
                else:
                    while self.board.changeable in visited:

                        self.board.changeable = random.choice(children)
                        j += 1
                        if j > 20:
                            if self.board.changeable not in noOptions:
                                noOptions.append(self.board.changeable)
                            for element in visited:
                                if element not in noOptions:
                                    self.board.changeable = element
                                break
                        break
        print(counter)
        print("WE HAVE FOUND IT!")
        return self.board


    """
    def breadFS(self):
        nodes = [] self.board.changeable
        beginState = self.changeable
        posMoves = checkPossibleMoves(beginState)
        for i in range(self.board.nrOfCars)
            for j rang(len(posMoves[j]))
                child = self.board.changeable
                child[i] = child[i] + posMoves[i][j]

        select

        #Create the first set of children
        for i in range(self.nrOfCars)
            for j rang(len(posMoves[j]))
                child = self.changeable
                child[i] = child[i] + posMoves[i][j]
                explored = []
                queue = [start]
                while true:
                    node = 




        while stack:
            cur_node = stack[0]
            stack = stack[1:]
            nodes.append(cur_node)
            moves = checkPossibleMoves()
            children 
            for child in cur_node.get_children():
                stack.append(child)
        return nodes
    """

