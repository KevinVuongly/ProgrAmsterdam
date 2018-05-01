import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class Board:
    """A class that describes the orientation of the board and allows and checks moves."""

    def __init__(self, gridSize, changeable, fixed, direction, length):
        """Initialisation of the board's parameters.

        Args:
            gridSize (int): An integer for the size of the grid.
            changeable (int): An int for the variable position of the car.
            fixed (int): An int for the fixed position of the car.
            direction (str): a character for the direction the car is facing.
            length (int): the length of a car.
            nrOfCars (int): the number of cars on the grid.

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
            vehicle (Int): The nr of the vehicle that is checked
            change (Int): The nr of places you want the vehicle to move, negative or positive, depending on direction
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

    

    def move(self, vehicle, change):
        check = self.checkMove(vehicle, change)

        if check == 0:
            self.changeable[vehicle] = self.changeable[vehicle] + change
        else:
            print("Move is illegal!")

    def visualize(self):
        grid = [["-" for x in range(self.gridSize)] for y in range(self.gridSize)]

        for j in range(self.length[0]):
            grid[self.fixed[0]][self.changeable[0] + j] = "*"

        for i in range(len(self.changeable)):
            if i > 0:
                if i + 97 < 127:
                    if self.direction[i] == "h":
                        for j in range(self.length[i]):
                            grid[self.fixed[i]][self.changeable[i] + j] = chr(i + 97)
                    else:
                        for j in range(self.length[i]):
                            grid[self.changeable[i] + j][self.fixed[i]] = chr(i + 97)
                else:
                    if self.direction[i] == "h":
                        for j in range(self.length[i]):
                            grid[self.fixed[i]][self.changeable[i] + j] = chr(i + 35)
                    else:
                        for j in range(self.length[i]):
                            grid[self.changeable[i] + j][self.fixed[i]] = chr(i + 35)

        for el in grid:
            print(" ".join(map(str, el)))

        image = np.zeros(self.gridSize * self.gridSize)

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                if grid[i][j] == "*":
                    image[self.gridSize * i + j] = 1
                elif grid[i][j] == "-":
                    image[self.gridSize * i + j] = 2
                else:
                    image[self.gridSize * i + j] = 3

        image = image.reshape((self.gridSize, self.gridSize))

        cmap = ListedColormap(['r', 'w', 'g'])
        plt.matshow(image, cmap=cmap)
        plt.show()

        