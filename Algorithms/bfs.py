from classes.Board import Board
import copy
import random

class Bfs:
    def __init__(self, board):
        """
        """
        self.board = board


    def randomSelection(self):
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

