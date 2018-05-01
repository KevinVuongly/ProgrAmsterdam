import numpy as np
import csv


class ReadBoard:
    """
    Read the csv-file. The very first row is the gridsize of the given game.
    Check game1.csv in the data folder to see how the csv-files are constructed.
    """
    
    def __init__(self, puzzle):
        """Initialisation of the board's parameters.

        Args:
            gridSize (int): An integer for the size of the grid.
            changeable (int): An int for the variable position of the car.
            fixed (int): An int for the fixed position of the car.
            length (int): the length of a car.
            nrOfCars (int): the number of cars on the grid.

        """

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
