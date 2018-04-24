import csv
import numpy as np

class Board:
    def __init__(self, puzzle):
        self.changeable = []
        self.fixed = []
        self.direction = []
        self.length = []

        with open(puzzle) as csvfile:
            readcsv = csv.reader(csvfile, delimiter = ",")

            self.gridSize = int(next(readcsv)[0])

            for row in readcsv:
                if row[2] == "h":
                    self.changeable.append(int(row[0]))
                    self.fixed.append(int(row[1]))
                else:
                    self.changeable.append(int(row[1]))
                    self.fixed.append(int(row[0]))

                self.direction.append(row[2])
                self.length.append(int(row[3]))

    def checkMove(self, vehicle, change):

        newPos = self.changeable[vehicle] + change

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
                    if usedElement[self.fixed[vehicle]][self.changable[vehicle] + self.length[vehicle] + i] == 1:
                        return 1
                else:
                    if usedElement[self.changable[vehicle] + self.length[vehicle] + i][self.fixed[vehicle]] == 1:
                        return 1
        else:
            for i in range(abs(change)):
                if self.direction[vehicle] == "h"
                    if usedElement[self.fixed[vehicle]][self.changable[vehicle] + self.length[vehicle] - 1 - i] == 1:
                        return 1
                else:
                    if usedElement[self.changable[vehicle] + self.length[vehicle] - 1 - i][self.fixed[vehicle]] == 1:
                        return 1

        return 0

    def move(self, vehicle, change):
        if checkMove(vehicle, change) == 0:
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

test = Board("../data/game1.csv")
test.checkMove()
