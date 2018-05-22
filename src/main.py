import time

from classes.Board import Board
from classes.ReadBoard import ReadBoard
from classes.Archive import Archive
from classes.Heuristics import Heuristic
from classes.Save import Save
from algorithms.random import Random
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.astar import Astar
from copy import copy, deepcopy

def main():

	data = pickGame()
<<<<<<< HEAD

	algorithms = ["random", "bfs", "astar", "dfs"]

	algorithm, game, beginState = pickAlgorithm(algorithms, data)

	heuristic = Heuristic(game)
	archive = Archive(heuristic)
	saveFile = Save(data, game, archive, beginState.colors)

	if algorithm.lower() == algorithms[0]:
		random = Random(game, archive)
		random.semiRandomSelection(saveFile)


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
		print("")

	elif algorithm.lower() == algorithms[3]:
		depthfs = DFS(game, archive)
		maxDepth = checkPositive("How many steps deep would you like to search: ")
		popAtMaxDepth = checkPositive("How much would you like to go back when that depth is reached: ")
		depthfs.dfs(saveFile, maxDepth, popAtMaxDepth)
		


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
		algorithm = input("Pick which algorithm you want to use(random, BFS, Astar, DFS): ")
		if algorithm.lower() not in algoList:
			print("Please pick a correct algorithm.")
		else:
			file = "data/game" + str(gameNumber) + ".csv"
=======

	algorithms = ["random", "bfs", "astar"]

	algorithm, game, beginState = pickAlgorithm(algorithms, data)
>>>>>>> 9a9f63e1d759f8f817ef26070618dc457492a060

	heuristic = Heuristic(game)
	archive = Archive(game, heuristic)
	saveFile = Save(data, game, archive, beginState.colors)

<<<<<<< HEAD
	return algorithm, game, beginState

def checkPositive(text):
	while True:
		value = input(text)
=======
	if algorithm.lower() == algorithms[0]:
		random = Random(game)

		solvedSteps = 240
		upperbound = 240
		solvedGame = []
		for i in range(100000):
			print("Fastest solution found so far: {} moves".format(solvedSteps))
			print("Try {}".format(i))
			newBoard = deepcopy(random)
			solvedGameTemp = newBoard.randomSelection(solvedSteps)
			solvedStepsTemp = len(solvedGameTemp)

			if solvedStepsTemp < solvedSteps:
				solvedSteps = solvedStepsTemp
				solvedGame = solvedGameTemp
				saveFile.saveSolution(solvedGame, "random")

	elif algorithm.lower() == algorithms[1]:
		types = ["normal", "heuristic", "beamsearch"]
>>>>>>> 9a9f63e1d759f8f817ef26070618dc457492a060

		try:
			value = int(value)
		except:
			print("Please give a positive, non-zero integer")

		if isinstance(value, int):
			if value <= 0:
				print("Please give a positive, non-zero integer")
			else:
<<<<<<< HEAD
=======
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
		loadGame = Astar(game, archive)

		solvedGame = loadGame.astar(saveFile)

		saveFile.saveSolution(solvedGame, "Astar")

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
>>>>>>> 9a9f63e1d759f8f817ef26070618dc457492a060
				break
	return value


<<<<<<< HEAD
				

=======
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
>>>>>>> 9a9f63e1d759f8f817ef26070618dc457492a060

	return algorithm, game, beginState

if __name__ == "__main__":
	main()
