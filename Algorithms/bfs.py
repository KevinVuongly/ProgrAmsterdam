from classes.Board import Board
import copy


class Bfs:
    def __init__(self, board):
        """Initialisation of the board's parameters.

        Args:
            gridSize (int): An integer for the size of the grid.
            changeable (list of ints): An int for the variable position of car i.
            fixed (list of ints): An int for the fixed position of car i.
            direction (list of strings): A character for the direction the car i is facing.
            length (list of ints): The length of car i.
            nrOfCars (int): The number of cars on the grid.
        """
        self.board = board




    def breadFS(self):
        nodes = []
        beginState = self.changeable
        posMoves = checkPossibleMoves(beginState)

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

