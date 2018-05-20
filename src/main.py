import time

from classes.Board import Board
from classes.ReadBoard import ReadBoard
from classes.Archive import Archive
from classes.Heuristics import Heuristic
from algorithms.random import Random
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from copy import copy, deepcopy

def main():

	while True:

		firstgame = 1
		lastgame = 7

		data = input("Pick the game you want to solve for (1, 2, 3,... , {}): ".format(lastgame))

		try:
			data = int(data)
		except:
			print("Please pick an existing game.")

		if isinstance(data, int):

			if data < firstgame or data > lastgame:
				print("Please pick an existing game.")
			else:
				break

	algorithms = ["random", "bfs"]

	while True:
		algorithm = input("Pick which algorithm you want to use(random, BFS): ")
		if algorithm.lower() not in algorithms:
			print("Please pick a correct algorithm.")
		else:
			file = "data/game" + str(data) + ".csv"

			beginState = ReadBoard(file)

			game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)

			break

	if algorithm.lower() == algorithms[0]:
		random = Random(game)

		solvedSteps = 100
		upperbound = 100
		solvedGame = []
		for i in range(5000):
			print("Fastest solution found so far: {} moves".format(solvedSteps))
			print("Try {}".format(i))
			newBoard = deepcopy(random)
			solvedGameTemp = newBoard.semiRandomSelection(solvedSteps)
			solvedStepsTemp = len(solvedGameTemp)
			if solvedStepsTemp < solvedSteps:
				solvedSteps = solvedStepsTemp
				solvedGame = solvedGameTemp
				print(solvedSteps)

		if solvedSteps < 180:
			print(solvedGame)
			for i in range(len(solvedGame)):
				game.visualize(solvedGame[i], beginState.colors, "random", data, i)

			saveSolution(solvedGame[len(solvedGame[i]) - 1], "random", data)

	elif algorithm.lower() == algorithms[1]:
		types = ["normal", "heuristic", "beamsearch"]

		while True:
			algoType = input("How do you want to use the breadth-first search algorithm?(normal, heuristic, beamSearch): ")

			if algoType.lower() not in types:
				print("Please pick a correct type.")
			else:
				heuristic = Heuristic(game)
				archive = Archive(heuristic)

				if algoType.lower() == types[0]:
					loadGame = BFS(data, game, archive, beginState.colors)
					solvedGame = loadGame.bfs()
					saveSolution(solvedGame, "BFS", data)

				elif algoType.lower() == types[1]:
					loadGame = BFS(data, game, archive, beginState.colors)
					solvedGame = loadGame.blockingRedCarHeuristic(Heuristic(game))
					saveSolution(solvedGame, "BFSheuristic", data)

				elif algoType.lower() == types[2]:
					loadGame = BFS(data, game, archive, beginState.colors)

					while True:

						width = input("What's the width you want to use for the beamsearch?: ")

						try:
							width = int(width)
						except:
							print("Please pick a feasible width.")

						if isinstance(width, int):

							if width < 0:
								print("Please pick a feasible width.")
							else:
								break

					solvedGame = loadGame.beamSearch(width)
					saveSolution(solvedGame, "BFSBeamSearch", data)

				break

def saveSolution(solutionState, gameType, game):
    textfile = "solutions/" + str(gameType) + "/" + str(game) + ".txt"

    with open(textfile, "w") as file:
        file.write("{}".format(solutionState))

if __name__ == "__main__":
	main()
