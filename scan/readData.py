import csv
import numpy as np

class game:
    def __init__(self, gridSize, puzzle):
        self.gridSize = gridSize

        self.changeable = []
        self.fixed = []
        self.richting = []
        self.lengte = []
        
        with open(puzzle) as csvfile:
            readcsv = csv.reader(csvfile, delimiter = ",")

            for row in readcsv:
                if row[2] == "0":
                    self.changeable.append(int(row[0]))
                    self.fixed.append(int(row[1]))
                else:
                    self.changeable.append(int(row[1]))
                    self.fixed.append(int(row[0]))

                self.richting.append(int(row[2]))
                self.lengte.append(int(row[3]))
        
    def visualize(self):
        grid = [["-" for x in range(self.gridSize)] for y in range(self.gridSize)]
  
        for i in range(len(self.changeable)):
            if self.richting[i] == 1:
                for j in range(self.lengte[i]):
                    grid[self.changeable[i] + j][self.fixed[i]] = chr(i + 97)
            else:
                for j in range(self.lengte[i]):
                    grid[self.fixed[i]][self.changeable[i] + j] = chr(i + 97)

        for el in grid:
            print(" ".join(map(str, el)))

test = game(6, "../data/game1.csv")
test.visualize()
