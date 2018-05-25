from classes.Board import Board
from classes.ReadBoard import ReadBoard

class Pick:
	""" Contains all functions asking for input. """
	def pickNumber(self, text, errortext, min, max):
		""" Checks if the input is an integer and if it's within feasible bounds.
			If the integer is not feasible, asks for a new input.

		Args:
			text (string): The initial text asking for the input.
			errortext (string): An error text when the input is illegal.
			min (int): The underbound of the domain.
			max (int): The upperbound of the domain.

		Return:
			value (int): If the input is legal, returns it.
		"""

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
		""" Asks for the algorithm the user wants to use.

		Args:
			algoList (list): List of all algoritms used in the solver.
			gameNumber (int): The game that the user wants to solve.

		Return:
			algorithm (string): The algorithm that the solver is now going to use.
			game (class): Contains all information of the game,
						  including all action that can be made with the game. 
			beginState (class): Contains all initial information of the game.
		"""
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
