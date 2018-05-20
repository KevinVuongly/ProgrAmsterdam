import numpy as np
import csv
import random

class ReadWriteStates:
    """

    """

    def __init__(self):
        """
        """

        self.states = []


    def readStates(self, path):

        with open(path) as csvfile:
            readcsv = csv.reader(csvfile)

            for row in readcsv:
                x = []
                for var in row:
                    x.append((var))
                self.states.append(x)

        return self.states


    def writeStates(self, solutionState, gameType, game):
        textfile = "solutions/" + str(gameType) + "/" + "game" + str(game) + ".csv"

        with open(textfile, "w") as file:
            writer = csv.writer(file, delimiter = ',')
            for row in solutionState:
                writer.writerow(row)



