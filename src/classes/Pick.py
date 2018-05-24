class Pick:

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
			beginState = ReadBoard(file)

			game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)

			break

	return algorithm, game, beginState

def checkPositive(text):
	while True:
		value = input(text)
		try:
			value = int(value)
		except:
			print("Please give a positive, non-zero integer")

		if isinstance(value, int):
			if value <= 0:
				print("Please give a positive, non-zero integer")
			else:
				break
	return value