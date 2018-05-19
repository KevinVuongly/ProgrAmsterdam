import time

import csv

from classes.ReadStates import ReadStates
from classes.Board import Board
from classes.ReadBoard import ReadBoard
from classes.Archive import Archive
from classes.Heuristics import Heuristic
from algorithms.random import Random
from algorithms.bfsBetweenStates import BFSBetweenStates
from algorithms.dfs import DFS
from copy import copy, deepcopy


class IterativeBfs:

    def __init__(self,gamejood):


    def iterativeBfs(self, gameNr, iterations, stepSize):




 


		file = "data/game" + str(gameNr) + ".csv"
		beginState = ReadBoard(file)
	
		game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)
	

		heuristic = Heuristic(game)
		archive = Archive(heuristic)
	



		path = "solutions/random/" + str(gameNr)  "2.csv"
		boardState = ReadStates(path)
		boardStates = boardState.readStates()



		startBoard = deepcopy(game)
		endBoard = deepcopy(game)

		lengthPath = len(boardStates)

		for j in range(0,iterations):
			if j == 0:
				newStates = deepcopy(boardStates)
			else:
				boardStates = newStates

			pathLength = len(boardStates)
			nrOfsteps = int(pathLength/stepSize)
			lastStep = pathLength%stepSize

			for i in range(0,nrOfsteps):
				newBoard = deepcopy(game)
				newArchive = deepcopy(archive)
				startingPoint = pathLength - (i+1)*stepSize -1
				endPoint = pathLength - i*stepSize - 1
				startingState = boardStates[startingPoint]
				endBoardstate = boardStates[endPoint]
				newBoard.changeable = startingState
				search = BFSBetweenStates(gameNr, newBoard, newArchive, beginState.colors, endBoardstate)
				result = search.bfsBetweenStates()
				newStates[startingPoint:endPoint] = result
			if lastStep != 0:
				startingPoint = 0
				endPoint = lastStep -1
				startingState = boardStates[startingPoint]
				endBoardstate = boardStates[endPoint]
				game.changeable = startingState
				newArchive = deepcopy(archive)
				newBoard = deepcopy(game)
				newBoard.changeable = startingState
				search = BFSBetweenStates(gameNr, newBoard, newArchive, beginState.colors, endBoardstate)
				result = search.bfsBetweenStates()
				newStates[startingPoint:endPoint] = result
				print("Before iterative BFS the game was solved in {} moves. After {} iterations with BFS stepsize of 15, it was solved in just {} moves".format(lengthPath, j + 1,len(newStates)))


		#print("Before iterative BFS the game was solved in {} moves. After 3 iterations with BFS stepsize of 15, it was solved in just {} moves".format(lengthPath,len(newStates)))

		saveSolution(newStates, "inbetweenstates", gameNr)

	"""
	for i in range(len(newStates)):
		game.visualize(newStates[i], beginState.colors, "improvedGame", game, i)

	for i in range(len(boardStates)):
		game.visualize(boardStates[i], beginState.colors, "oldGame", game, i)
	"""



def saveSolution(solutionState, gameType, game):
    textfile = "solutions/" + str(gameType) + "/" + "game" + str(game) + ".csv"

    with open(textfile, "w") as file:
        writer = csv.writer(file, delimiter = ',')
        for row in solutionState:
        	writer.writerow(row)




if __name__ == "__main__":
	main()