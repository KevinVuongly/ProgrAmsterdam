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


def main():


	# READING IN

	gameNr = 2

 


	file = "data/game2.csv"
	beginState = ReadBoard(file)
	

	game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)
	

	heuristic = Heuristic(game)
	archive = Archive(heuristic)
	


	path = "solutions/random/2.csv"
	boardState = ReadStates(path)
	boardStates = boardState.readStates()



	startBoard = deepcopy(game)
	endBoard = deepcopy(game)

	lengthPath = len(boardStates)


	for j in range(0,5):
		if j == 0:
			newStates = deepcopy(boardStates)
		else:
			boardStates = deepcopy(newStates)

		stepSize = 6	
		jumps = stepSize + 1 #take one extra, to avoid using same ones twice
		pathLength = len(boardStates)
		nrOfsteps = int(pathLength/jumps)
		lastStep = pathLength%jumps
		end = 1
		start = stepSize + 1
		solution = []



		for i in range(0,nrOfsteps):
			newBoard = deepcopy(game)
			newArchive = deepcopy(archive)
			startingState = boardStates[start]
			endBoardstate = boardStates[end]
			print("start = {}, end = {}: ".format(boardStates.index(startingState), boardStates.index(endBoardstate)))
			newBoard.changeable = startingState
			search = BFSBetweenStates(gameNr, newBoard, newArchive, beginState.colors, endBoardstate)
			result = search.bfsBetweenStates()
			solution = solution + result
			start = end + 1 
			end = start + stepSize
			newStates = solution
		if lastStep != 0 and (lastStep - 1) != 0:   # if laststep -1 is zero it will bfs from 0 to 0
			start = -lastStep
			end = - 1
			startingState = boardStates[start]
			endBoardstate = boardStates[end]
			newArchive = deepcopy(archive)
			newBoard = deepcopy(game)
			newBoard.changeable = startingState
			search = BFSBetweenStates(gameNr, newBoard, newArchive, beginState.colors, endBoardstate)
			result = search.bfsBetweenStates()
			solution = solution + result


			
		print("let's loop again friends")
		newstates = remove_duplicates(solution)
		print("Before iterative BFS the game was solved in {} moves. After {} iterations with BFS stepsize of {}, it was solved in just {} moves".format(lengthPath, j + 1, stepSize, len(newStates)))


	#print("Before iterative BFS the game was solved in {} moves. After 3 iterations with BFS stepsize of 15, it was solved in just {} moves".format(lengthPath,len(newStates)))

	saveSolution(newStates, "inbetweenstates", gameNr)

	
	for i in range(len(newStates)):
		game.visualize(newStates[i], beginState.colors, "improvedGame", game, i)

	"""
	for i in range(len(boardStates)):
		game.visualize(boardStates[i], beginState.colors, "oldGame", game, i)
	"""



def saveSolution(solutionState, gameType, game):
    textfile = "solutions/" + str(gameType) + "/" + "game" + str(game) + ".csv"

    with open(textfile, "w") as file:
        writer = csv.writer(file, delimiter = ',')
        for row in solutionState:
        	writer.writerow(row)

def remove_duplicates(values):
    output = []

    for value in values:
        if value not in output:
            output.append(value)
    return output



if __name__ == "__main__":
	main()