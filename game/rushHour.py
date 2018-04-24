import csv
import numpy as np

class car:
    def __init__(self, puzzle):
        self.changeable = []
        self.fixed = []
        self.richting = []
        self.lengte = []

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

                self.richting.append(row[2])
                self.lengte.append(int(row[3]))

    def visualize(self):
        grid = [["-" for x in range(self.gridSize)] for y in range(self.gridSize)]

        for j in range(self.lengte[0]):
            grid[self.fixed[0]][self.changeable[0] + j] = "*"

        for i in range(len(self.changeable)):
            if i > 0:
                if i + 97 < 127:
                    if self.richting[i] == "v":
                        for j in range(self.lengte[i]):
                            grid[self.changeable[i] + j][self.fixed[i]] = chr(i + 97)
                    else:
                        for j in range(self.lengte[i]):
                            grid[self.fixed[i]][self.changeable[i] + j] = chr(i + 97)
                else:
                    if self.richting[i] == "v":
                        for j in range(self.lengte[i]):
                            grid[self.changeable[i] + j][self.fixed[i]] = chr(i + 35)
                    else:
                        for j in range(self.lengte[i]):
                            grid[self.fixed[i]][self.changeable[i] + j] = chr(i + 35)

        for el in grid:
            print(" ".join(map(str, el)))

test = car("../data/game7.csv")
test.visualize()
