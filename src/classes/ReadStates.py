import numpy as np
import csv
import random

class ReadStates:
    """ Read a csv-file with a path containing only the changeables. """

    def __init__(self, path):
        """ Initialization of ReadStates' parameters.

        Initialization:
            self.states: Initializate empty array to fill with states

        Args:
            path (string): Containing the path to the csv file
        """

        self.states = []
        self.path = path


    def readStates(self):
        """ Reads the states in row for row and returns the path

        Return:
            States (list of lists): Returns the changeable path from the csv file.
        """

        with open(self.path) as csvfile:
            readcsv = csv.reader(csvfile)

            for row in readcsv:
                x = []
                for var in row:
                    x.append(int(var))
                self.states.append(x)

        return self.states






