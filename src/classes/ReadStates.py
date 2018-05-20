import numpy as np
import csv
import random

class ReadStates:
    """

    """

    def __init__(self, path):
        """
        """

        self.states = []
        self.path = path


    def readStates(self):


        with open(self.path) as csvfile:
            readcsv = csv.reader(csvfile)

            for row in readcsv:
                x = []
                for var in row:
                    x.append(int(var))
                self.states.append(x)

        return self.states






