import time

from classes.Board import Board
from classes.ReadBoard import ReadBoard
from classes.Archive import Archive
from classes.Heuristics import Heuristic
from classes.Save import Save
from algorithms.random import Random
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from copy import copy, deepcopy

def main():

	data = pickGame()

	algorithms = ["random", "bfs", "astar"]

	algorithm, game, beginState = pickAlgorithm(algorithms, data)

	heuristic = Heuristic(game)
	archive = Archive(heuristic)
	saveFile = Save(data, game, archive, beginState.colors)

	if algorithm.lower() == algorithms[0]:
		random = Random(game)

		solvedSteps = 240
		upperbound = 240
		solvedGame = []
		for i in range(100000):
			print("Fastest solution found so far: {} moves".format(solvedSteps))
			print("Try {}".format(i))
			newBoard = deepcopy(random)
			solvedGameTemp = newBoard.semiRandomSelection(solvedSteps)
			solvedStepsTemp = len(solvedGameTemp)

			if solvedStepsTemp < solvedSteps:
				solvedSteps = solvedStepsTemp
				solvedGame = solvedGameTemp
				saveFile.saveSolution(solvedGame, "random")

	elif algorithm.lower() == algorithms[1]:
		types = ["normal", "heuristic", "beamsearch"]

		while True:
			algoType = input("How do you want to use the breadth-first search algorithm?(normal, heuristic, beamSearch): ")

			if algoType.lower() not in types:
				print("Please pick a correct type.")
			else:
				loadGame = BFS(game, archive)

				solvedGame = loadGame.bfs(algoType.lower(), saveFile)

				if algoType.lower() == types[0]:
					saveFile.saveSolution(solvedGame, "BFS")
				elif algoType.lower() == types[1]:
					saveFile.saveSolution(solvedGame, "BFSheuristic")
				elif algoType.lower() == types[2]:
					saveFile.saveSolution(solvedGame, "BFSBeamSearch")

				break

	elif algorithm.lower() == algorithms[2]:
		continue

def pickGame():
	while True:

		firstgame = 1
		lastgame = 7

		gameNumber = input("Pick the game you want to solve for (1, 2, 3,... , {}): ".format(lastgame))

		try:
			gameNumber = int(gameNumber)
		except:
			print("Please pick an existing game.")

		if isinstance(gameNumber, int):

			if gameNumber < firstgame or gameNumber > lastgame:
				print("Please pick an existing game.")
			else:
				break

	return gameNumber

def pickAlgorithm(algoList, gameNumber):
	while True:
		algorithm = input("Pick which algorithm you want to use(random, BFS, Astar): ")
		if algorithm.lower() not in algoList:
			print("Please pick a correct algorithm.")
		else:
			file = "data/game" + str(gameNumber) + ".csv"

			beginState = ReadBoard(file)

			game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)

			break

	return algorithm, game, beginState

if __name__ == "__main__":
	main()
