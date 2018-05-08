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
		algorithm = input("Pick which algorithm you want to use(random, BFS): ")
		if algorithm != "random" and algorithm != "BFS":
			print("Please pick a correct algorithm.")
		else:
			file = "data/game" + str(data) + ".csv"

			beginState = ReadBoard(file)

			game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)

			print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Running algorithm...")
			break

	archive = Archive()

	if algorithm == "random":
		random = Random(game)

		solvedSteps = 1003
		solvedGame = []
		for i in range(100):
			print("Fastest solution found so far: {} moves".format(solvedSteps))
			print("Try {}".format(i))
			newBoard = deepcopy(random)
			solvedGameTemp = newBoard.semiRandomSelection(solvedSteps)
			solvedStepsTemp = len(solvedGameTemp)
			if solvedStepsTemp < solvedSteps:
				solvedSteps = solvedStepsTemp
				solvedGame = solvedGameTemp
				print(solvedSteps)

		
		if solvedSteps < 1000:
			print(solvedGame)
			for i in range(len(solvedGame))`:
				game.visualize(solvedGame[i], beginState.colors, "random", data, i)


		

	elif algorithm == "BFS":
		loadGame = BFS(data, game, archive, beginState.colors)
		solvedgame = loadGame.bfs()

	print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Solution found.")

if __name__ == "__main__":
	main()
