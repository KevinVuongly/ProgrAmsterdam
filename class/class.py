import csv
import numpy as np

"""
Read the csv-file. The very first row is the gridsize of the given game.
"""
class ReadBoard:
    def __init__(self, puzzle):
        self.changeable = []
        self.fixed = []
        self.direction = []
        self.length = []

        with open(puzzle) as csvfile:
            readcsv = csv.reader(csvfile, delimiter = ",")

            self.gridSize = int(next(readcsv)[0])

            next(readcsv)

            for row in readcsv:
                xCar = row[0]
                yCar = row[1]
                directionCar = row[2]
                lengthCar = row[3]

                if directionCar == "h":
                    self.changeable.append(int(xCar))
                    self.fixed.append(int(yCar))
                else:
                    self.changeable.append(int(yCar))
                    self.fixed.append(int(xCar))

                self.direction.append(directionCar)
                self.length.append(int(lengthCar))

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

        for el in grid:
            print(" ".join(map(str, el)))

data = ReadBoard("../data/game1.csv")
game = Board(data.gridSize, data.changeable, data.fixed, data.direction, data.length)
print(game.checkMove(1,2))
