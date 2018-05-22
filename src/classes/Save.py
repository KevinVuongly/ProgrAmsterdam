from copy import copy
import csv
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class Save:
    def __init__(self, gameNumber, board, archive, colors):
        self.gameNumber = gameNumber
        self.board = board
        self.archive = archive
        self.colors = colors

    def createGrid(self, changeable):
        """
        Creates a matrix representation of the board
        """
        grid = [["-" for x in range(self.board.gridSize)] for y in range(self.board.gridSize)]

        for j in range(self.board.length[0]):
            grid[self.board.fixed[0]][changeable[0] + j] = "*"

        for i in range(1, self.board.nrOfCars):
            if i + 97 < 127:
                if self.board.direction[i] == "h":
                    for j in range(self.board.length[i]):
                        grid[self.board.fixed[i]][changeable[i] + j] = chr(i + 97)
                else:
                    for j in range(self.board.length[i]):
                        grid[changeable[i] + j][self.board.fixed[i]] = chr(i + 97)
            else:
                if self.board.direction[i] == "h":
                    for j in range(self.board.length[i]):
                        grid[self.board.fixed[i]][changeable[i] + j] = chr(i + 35)
                else:
                    for j in range(self.board.length[i]):
                        grid[changeable[i] + j][self.board.fixed[i]] = chr(i + 35)

        return grid

    def visualize(self, changeable, move, folder):
        """
        Visualizes the current state of the board.
        """
        boardGrid = self.createGrid(changeable)

        image = np.zeros(self.board.gridSize * self.board.gridSize)

        for k in range(self.board.nrOfCars):
            for i in range(self.board.gridSize):
                for j in range(self.board.gridSize):
                    if boardGrid[i][j] == "*":
                        image[self.board.gridSize * i + j] = 1
                    elif boardGrid[i][j] == "-":
                        image[self.board.gridSize * i + j] = 2
                    elif boardGrid[i][j] == chr(k + 97) or boardGrid[i][j] == chr(k + 35):
                        image[self.board.gridSize * i + j] = 3 + k

        image = image.reshape((self.board.gridSize, self.board.gridSize))

        cmap = ListedColormap(self.colors)
        plt.matshow(image, cmap=cmap)

        figname = folder + "/Move" + str(move) + ".png"
        plt.savefig(figname)

        print("Move {} saved.".format(move))
        plt.close()

    def createFolder(self, gameType):
        """ Creates a new folder for the solution to save in. """
        folder = "solutions/" + str(gameType) + "/" + str(self.gameNumber)

        if os.path.exists(folder):
            shutil.rmtree(folder, ignore_errors=True)
            os.makedirs(folder)

        return folder

    def pathSolution(self, solutionState, foldername):
        """ Visualizes the path found through breadth first search. """
        self.path = [solutionState]

        child = copy(solutionState)

        parent = self.archive.visitedStates[str(child)]

        while self.archive.visitedStates[str(child)] != "beginning!":
            self.path.insert(0, parent)

            child = parent
            parent = self.archive.visitedStates[str(child)]

        folder = self.createFolder(foldername)

        for i in range(len(self.path)):
            self.visualize(self.path[i], i, folder)

    def saveSolution(self, lastMove, gameType):
        """ Saves the found solution into a .csv and the end solutionstate in a .txt. """
        textfile = "solutions/" + str(gameType) + "/" + str(self.gameNumber)

        with open(textfile + ".csv", "w") as csvfile:
            writer = csv.writer(csvfile, delimiter = ",")

            for row in self.path:
                writer.writerow(row)

        with open(textfile + ".txt", "w") as textfile:
    	    textfile.write("{}".format(lastMove))
