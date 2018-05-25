from copy import copy
import csv
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class Save:
    """ A class containing all save-actions when the game is solved for."""
    def __init__(self, gameNumber, board, archive, colors):
        """ Initialization of the parameters.

        Args:
            gameNumber (int): The game that is solved for.
            board (class): Containing all information of the (solved!) game.
            archive (class): Containing the archive class, including the archive itself.
            colors (list): The colors of all the cars.

        Initialization:
            endStateFolder: The folder where the last move will be saved in.
        """

        self.gameNumber = gameNumber
        self.board = board
        self.archive = archive
        self.colors = colors

        self.endStateFolder = "solutions/endSolution/"

    def createGrid(self, changeable):
        """ Creates a matrix representation of the current state of the game.

        Initialization:
            grid (list of lists): An empty grid according to the gamesize.

        Args:
            changeable (list): The current state of the game.

        Return:
            grid (list of lists): The referred matrix representation.
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
        """ Visualizes the given state of the game.

        Initialization:
            boardGrid: Create the matrix representation of the current state of the game.
            image: Initialize the image, which is empty at first-hand.

        Args:
            changeable (list): The current state of the game.
            move (int): The amount of moves made to get to this state.
            folder (string): The folder where the visualization has to be saved in
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
        """ Creates a new folder for the solution to save in.
            If it already exists, re-creates it.

        Args:
            gameType (string): The algorithm that is used to solve the game.

        Return:
            folder (string): The created folder.
        """
        folder = "solutions/" + str(gameType) + "/" + str(self.gameNumber)

        if os.path.exists(folder):
            shutil.rmtree(folder, ignore_errors=True)
        os.makedirs(folder)

        return folder

    def pathSolution(self, solutionState, folderName, astar=False, dfs=False):
        """ Creates then visualizes the path according to the algorithm.

        Initalization:
            path: The path of the solution, initially it only contains the ending.

        Args:
            solutionState (list): The end of the path, which is a solution of the game.
            folderName (string): The algorithm that is used to solve the game,
                                 used as the name for the folder.
            astar (boolean): True if the A*-algorithm is used, false if not.
            dfs (boolean): True if the depth-first search algorithm is used, false if not.
        """
        self.path = [solutionState]

        child = copy(solutionState)

        if astar == True or dfs == True:
            if astar == True:
                self.createPathSolutionAStar(child)
            else:
                self.createPathSolutionDFS(child)
        else:
            self.createPathSolution(child)

        folder = self.createFolder(folderName)

        for i in range(len(self.path)):
            self.visualize(self.path[i], i, folder)

    def createPathSolution(self, child):
        """ Creates the path using the archive by updating self.path.

        Args:
            child (list): The initial child, which is the end of the path.
        """
        parent = self.archive.visitedStates[str(child)]

        while parent != "beginning!":
            self.path.insert(0, parent)

            child = parent
            parent = self.archive.visitedStates[str(child)]

    def createPathSolutionAStar(self, child):
        """ Creates the path using the archive.
            The A*-algorithm has it's own unique value layout for the archive.

        Args:
            child (list): The initial child, which is the end of the path.
        """
        parent = self.archive.visitedStates[str(child)][1]

        while parent != "beginning!":
            self.path.insert(0, parent)

            child = parent
            parent = self.archive.visitedStates[str(child)][1]

    def createPathSolutionDFS(self, child):
        """ Creates the path using the archive
            The DFS-algorithm has it's own unique value layout for the archiveself.

        Args:
            child (list): The initial child, which is the end of the path.
        """
        parent = self.archive.visitedStates[str(child)][0]

        while self.archive.visitedStates[str(child)][0] != "beginning!":
            self.path.insert(0, parent)

            child = parent
            parent = self.archive.visitedStates[str(child)][0]

    def getPath(self, solutionState):
        """ Get's the path of the solution, needed for the experiments.

        Args:
            solutionState (list): Last state of the solution e.g. last move.

        Return:
            path (list of lists): The path of the solution.
        """
        path = [solutionState]

        child = copy(solutionState)
        parent = self.archive.visitedStates[str(child)]

        while self.archive.visitedStates[str(child)] != "beginning!":
            path.insert(0, parent)

            child = parent
            parent = self.archive.visitedStates[str(child)]

        return path

    def saveSolution(self, lastMove, gameType):
        """ Saves the found solution into a .csv and the end solutionstate in a .txt.

        Args:
            lastMove (list): The last move made of the solution.
            gameType (string): The algorithm that is used by the solver.
        """

        filename = "solutions/" + str(gameType) + "/" + str(self.gameNumber)

        with open(filename + ".csv", "w") as csvfile:
            writer = csv.writer(csvfile, delimiter = ",")

            for row in self.path:
                writer.writerow(row)

        self.saveEndSolution(lastMove)

    def saveEndSolution(self, lastMove):
        """ Saves the end solutionSate in a .txt file. Reason to split this in it's own function
            is because the path isn't relevant for the random algorithm.

        Args:
        lastMove (list): The last move made of the solution.
        """

        print()
        print("Saving the last move in {}.".format(self.endStateFolder))

        with open(self.endStateFolder + str(self.gameNumber) + ".txt", "w") as textfile:
            textfile.write("{}".format(lastMove))
