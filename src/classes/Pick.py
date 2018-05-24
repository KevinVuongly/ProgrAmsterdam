from classes.Board import Board
from classes.ReadBoard import ReadBoard

class Pick:
	""" Contains all functions asking for input. """
	def pickNumber(self, text, errortext, min, max):
		while True:

			value = input(text)

			try:
				value = int(value)
			except:
				print(errortext)

			if isinstance(value, int):

				if not min <= value <= max:
					print(errortext)
				else:
					break

		return value

	def pickAlgorithm(self, algoList, gameNumber):
		while True:
			algorithm = input("Pick which algorithm you want to use(BFS, Astar, DFS): ")
			if algorithm.lower() not in algoList:
				print("Please pick a correct algorithm.")
			else:
				file = "data/game" + str(gameNumber) + ".csv"
				beginState = ReadBoard(file)

				game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)

				break

		return algorithm, game, beginState
