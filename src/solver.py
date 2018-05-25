import time

from classes.Pick import Pick
from classes.Archive import Archive
from classes.Heuristics import Heuristic
from classes.Save import Save
from classes.Endpoint import EndPoint
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.astar import Astar
from copy import copy, deepcopy
import math

def solver():
	pick = Pick()

	firstgame = 1
	lastgame = 7
	initText = "Pick the game you want to solve for (1, 2, 3,... , {}): ".format(lastgame)
	initErrorText = "Please pick an existing game."

	data = pick.pickNumber(initText, initErrorText, firstgame, lastgame)

	algorithms = ["bfs", "astar", "dfs"]

	algorithm, game, beginState = pick.pickAlgorithm(algorithms, data)

	heuristic = Heuristic(game)
	archive = Archive(game, heuristic)
	saveFile = Save(data, game, archive, beginState.colors)

	if algorithm.lower() == algorithms[0]:
		types = ["normal", "heuristic", "beamsearch"]

		while True:
			algoType = input("How do you want to use the breadth-first search algorithm?(normal, heuristic, beamSearch): ")

			if algoType.lower() not in types:
				print("Please pick a correct type.")
			else:
				endPoint = EndPoint(deepcopy(game), deepcopy(archive), deepcopy(saveFile))
				loadGame = BFS(game, archive, endPoint)

				solvedGame = loadGame.bfs(algoType.lower(), saveFile)

				if algoType.lower() == types[0]:
					saveFile.saveSolution(solvedGame, "BFS")
				elif algoType.lower() == types[1]:
					saveFile.saveSolution(solvedGame, "BFSheuristic")
				elif algoType.lower() == types[2]:
					saveFile.saveSolution(solvedGame, "BFSBeamSearch")

				break

	elif algorithm.lower() == algorithms[1]:
		endPoint = EndPoint(deepcopy(game), deepcopy(archive), deepcopy(saveFile))
		loadGame = Astar(game, archive, endPoint, saveFile)

		solvedGame = loadGame.astar()

		saveFile.saveSolution(solvedGame, "Astar")

	elif algorithm.lower() == algorithms[2]:
		depthfs = DFS(game, archive)

		text = "How many steps deep would you like to search: "
		errorText = "Please give a positive, non-zero integer."
		min = 1
		max = math.inf

		maxDepth = pick.pickNumber(text, errorText, min, max)

		text = "How much would you like to go back when that depth is reached: "
		popAtMaxDepth = pick.pickNumber(text, errorText, min, max)

		depthfs.dfs(saveFile, maxDepth, popAtMaxDepth)

if __name__ == "__main__":
	solver()
