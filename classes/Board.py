import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class Board:
    """A class that describes the orientation of the board and allows and checks moves."""

    def __init__(self, gridSize, changeable, fixed, direction, length):
        """Initialisation of the board's parameters.

        Args:
            gridSize (int): An integer for the size of the grid.
            changeable (list of ints): An int for the variable position of car i.
            fixed (list of ints): An int for the fixed position of car i.
            direction (list of strings): A character for the direction the car i is facing.
            length (list of ints): The length of car i.
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
            vehicle (Int): The number of the vehicle that is checked.
            change (Int): The number of places you want the vehicle to move,
                          negative or positive, depending on direction.
        """

        newPos = self.changeable[vehicle] + change
        if not isinstance(change, int):
            return 1

        if newPos < 0 or newPos > self.gridSize - self.length[vehicle]:
            return 1

        usedElement = [[0 for x in range(self.gridSize)] for y in range(self.gridSize)]

        for i in range(len(self.changeable)):
            for j in range(self.length[i]):
                if self.direction[i] == "h":
                    usedElement[self.fixed[i]][self.changeable[i] + j] = 1
                else:
                    usedElement[self.changeable[i] + j][self.fixed[i]] = 1


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

    def checkPossibleMoves(self):
        """
        Checks all possible moves of a given state.
        """

        if checkSolution == 0:
            return = 0
            print("solved")

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
            possiblemovesarray.append(possibleMoves)

        print(possiblemovesarray)

    def checkSolution(self):
        movesToEndblock = self.gridSize - self.changeable[0] - 2
        if self.checkMove(0,movesToEndblock) == 0:
            return 0
        return 1

    def move(self, vehicle, change):
        check = self.checkMove(vehicle, change)

        if check == 0:
            self.changeable[vehicle] = self.changeable[vehicle] + change
        else:
            print("Move is illegal!")

    """
    Visualizes the current state of the board.
    """
    def visualize(self, changeable, colors):
        grid = [["-" for x in range(self.gridSize)] for y in range(self.gridSize)]

        for j in range(self.length[0]):
            grid[self.fixed[0]][changeable[0] + j] = "*"

        for i in range(1, len(self.changeable)):
            if i + 97 < 127:
                if self.direction[i] == "h":
                    for j in range(self.length[i]):
                        grid[self.fixed[i]][changeable[i] + j] = chr(i + 97)
                else:
                    for j in range(self.length[i]):
                        grid[changeable[i] + j][self.fixed[i]] = chr(i + 97)
            else:
                if self.direction[i] == "h":
                    for j in range(self.length[i]):
                        grid[self.fixed[i]][changeable[i] + j] = chr(i + 35)
                else:
                    for j in range(self.length[i]):
                        grid[changeable[i] + j][self.fixed[i]] = chr(i + 35)

        image = np.zeros(self.gridSize * self.gridSize)

        for k in range(self.nrOfCars):
            for i in range(self.gridSize):
                for j in range(self.gridSize):
                    if grid[i][j] == "*":
                        image[self.gridSize * i + j] = 1
                    elif grid[i][j] == "-":
                        image[self.gridSize * i + j] = 2
                    elif grid[i][j] == chr(k + 97) or grid[i][j] == chr(k + 35):
                        image[self.gridSize * i + j] = 3 + k

        image = image.reshape((self.gridSize, self.gridSize))

        cmap = ListedColormap(colors)
        plt.matshow(image, cmap=cmap)
        plt.show()
