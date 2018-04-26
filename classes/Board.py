import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

"""
A class that describes the orietntation of the board and allows and checks moves.
"""


class Board:
    def __init__(self, gridSize, changeable, fixed, direction, length):
        self.gridSize = gridSize
        self.changeable = changeable
        self.fixed = fixed
        self.direction = direction
        self.length = length


    def checkMove(self, vehicle, change):
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

        for el in usedElement:
            print(" ".join(map(str, el)))

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

    def checkPossibleMoves(self)
        minimalChange = - self.length - 1
        maximalChange = self.legth - 1 
        nrOfCars = len(self.changeable)

        for j in range(nrOfCars):
            for i in range(minimalChange,maximalChange):
                if checkMove(j, i) == 0
                    append(possiblemovesarray)




    def move(self, vehicle, change):
        check = checkMove(vehicle, change)


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
        """
        Als we de waardes hiervoor (a,b en c veranderen naar waardes (dus chr en 97 en 35 weghalen,
            dan krijgen we 0 1 2 etc voor alle auto'tjes. Deze kunnnen we dan omzetten naar een gridmap,
            zodat we een hele checke visualisatie krijgen zoals op deze site: 
            https://stackoverflow.com/questions/518021/getting-the-length-of-an-array-in-python.
            of google naar gridmap python, dan krijg je andere voorbeelden.))


        # create discrete colormap
        cmap = colors.ListedColormap(['red', 'blue'])
        bounds = [0,10,20]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(data, cmap=cmap, norm=norm)

        # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-.5, 10, 1));
        ax.set_yticks(np.arange(-.5, 10, 1));

        plt.show()

        for el in grid:
            print(" ".join(map(str, el)))

        """

data = ReadBoard("../data/game1.csv")
game = Board(data.gridSize, data.changeable, data.fixed, data.direction, data.length)
print(game.checkMove(1,2))
