from copy import copy, deepcopy

class Board:
    """A class that describes the orientation of the board and allows and checks moves."""

    def __init__(self, gridSize, changeable, fixed, direction, length):
        """Initialisation of the board's parameters.

        Args:
            gridSize (int): An integer for the size of the grid.
            changeable (array of ints): An int for the variable position of car i.
            fixed (array of ints): An int for the fixed position of car i.
            direction (array of strings): A character for the direction the car i is facing.
            length (array of ints): The length of car i.
            nrOfCars (int): The number of cars on the grid.
        """

        self.gridSize = gridSize
        self.changeable = changeable
        self.fixed = fixed
        self.direction = direction
        self.length = length
        self.nrOfCars = len(changeable)

    def checkMove(self, vehicle, change):
        """Checks if the move is feasible.

        Args:
            vehicle (int): The number of the vehicle that is checked.
            change (int): The number of places you want the vehicle to move,
                          negative or positive, depending on direction.
        """

        newPos = self.changeable[vehicle] + change
        if not isinstance(change, int):
            return 1

        if newPos < 0 or newPos > self.gridSize - self.length[vehicle]:
            return 1

        usedElement = self.occupiedElements()

        if change > 0:
            for i in range(change):
                if self.direction[vehicle] == "h":
                    if usedElement[self.fixed[vehicle]][self.changeable[vehicle] + self.length[vehicle] + i] == 1:
                        return 1
                else:
                    if usedElement[self.changeable[vehicle] + self.length[vehicle] + i][self.fixed[vehicle]] == 1:
                        return 1
        else:
            for i in range(abs(change)):
                if self.direction[vehicle] == "h":
                    if usedElement[self.fixed[vehicle]][self.changeable[vehicle] - 1 - i] == 1:
                        return 1
                else:
                    if usedElement[self.changeable[vehicle] - 1 - i][self.fixed[vehicle]] == 1:
                        return 1
        return 0

    def occupiedElements(self):
        """ Returns a grid that shows the occupation of an element.

        If an element is occupied it gets the value of 1. Else, 0.
        """
        occupiedMatrix = [[0 for x in range(self.gridSize)] for y in range(self.gridSize)]

        for i in range(len(self.changeable)):
            for j in range(self.length[i]):
                if self.direction[i] == "h":
                    occupiedMatrix[self.fixed[i]][self.changeable[i] + j] = 1
                else:
                    occupiedMatrix[self.changeable[i] + j][self.fixed[i]] = 1

        return occupiedMatrix

    def checkPossibleMoves(self):
        """ Checks all possible moves of a given state. """
        possiblemovesarray = []


        for j in range(self.nrOfCars):
            minMaxChange = self.gridSize - self.length[j] + 1
            possibleMoves = []

            for i in range(1,minMaxChange):
                if self.checkMove(j, i) == 0:
                    possibleMoves.append(i)
                else:
                    break
            for i in range(1,minMaxChange):
                if self.checkMove(j, -i) == 0:
                    possibleMoves.append(-i)
                else:
                    break

            possibleMovesArray.append(possibleMoves)

        return possibleMovesArray

    def createChildren(self):
        """ Creates the children for given board. """
        children = []
        posMoves = self.checkPossibleMoves()

        for i in range(self.nrOfCars):
            if len(posMoves[i]) > 0:
                for j in range(len(posMoves[i])):
                    child = copy(self.changeable)
                    child[i] = child[i] + posMoves[i][j]
                    children.append(child)
        return children

    def checkSolution(self):
        """ Checks if board is solved and returns 0 if so. """
        movesToEndblock = self.gridSize - self.changeable[0] - 2
        if self.checkMove(0,movesToEndblock) == 0:
            return 0
        return 1
