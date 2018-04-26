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