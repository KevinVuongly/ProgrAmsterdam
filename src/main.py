import time

from classes.Board import Board
from classes.ReadBoard import ReadBoard
from classes.Archive import Archive
from algorithms.random import Random
from algorithms.bfs import BFS
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

	while True:
		algorithm = input("Pick which algorithm you want to use(random, BFS, BFSheuristic): ")
		if algorithm != "random" and algorithm != "BFS" and algorithm != "BFSheuristic":
			print("Please pick a correct algorithm.")
		else:
			file = "data/game" + str(data) + ".csv"

			beginState = ReadBoard(file)

			game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)

			print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Running algorithm...")
			break


	if algorithm == "random":
		random = Random(game)

<<<<<<< HEAD
		solvedSteps = 180
=======
<<<<<<< HEAD
		solvedSteps = 1500
		upperbound = 1500
		solvedGame = []
		for i in range(5000):
			print(solvedSteps)
=======
		solvedSteps = 1181
>>>>>>> d32f298a3fcb3b6b65600af3b100a807adb7046b
		solvedGame = []
		for i in range(150000):
			print("Fastest solution found so far: {} moves".format(solvedSteps))
			print("Try {}".format(i))
>>>>>>> 3a6d6a90d33f0dc71b18cbe50fbf3d6210023e76
			newBoard = deepcopy(random)
			solvedGameTemp = newBoard.semiRandomSelection(solvedSteps)
			solvedStepsTemp = len(solvedGameTemp)
			if solvedStepsTemp < solvedSteps:
				solvedSteps = solvedStepsTemp
				solvedGame = solvedGameTemp
				print(solvedSteps)

<<<<<<< HEAD
		if solvedSteps < upperbound:
			for i in range(len(solvedGame)):
				game.visualize(solvedGame[i], beginState.colors, "random", data, i)
=======
		
		if solvedSteps < 180:
			print(solvedGame)
			for i in range(len(solvedGame)):
				game.visualize(solvedGame[i], beginState.colors, "random", data, i)



>>>>>>> 3a6d6a90d33f0dc71b18cbe50fbf3d6210023e76

	elif algorithm == "BFS":
		loadGame = BFS(data, game, archive, beginState.colors)
		solvedgame = loadGame.bfs()

	elif algorithm == "BFSheuristic":
		loadGame = BFS(data, game, archive, beginState.colors)
		solvedgame = loadGame.bfsHeuristic()

	print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.")

if __name__ == "__main__":
	main()
