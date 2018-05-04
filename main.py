from classes.Board import Board
from classes.ReadBoard import ReadBoard
from algorithms.random import Random
from algorithms.bfs import BFS

def main():

	while True:
		data = input("Pick the game you want to solve for (1, 2, 3,... , 7): ")

		try:
			data = int(data)
		except:
			print("Please pick an existing game.")

		if isinstance(data, int):
			firstgame = 1
			lastgame = 7

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

			break

	if algorithm == "random":
		loadGame = Random(game)

		solvedgame = loadGame.randomSelection()
		solvedgame.visualize(solvedgame.changeable, beginState.colors)
	elif algorithm == "BFS":
		loadGame = BFS(data, game, beginState.colors)
		solvedgame = loadGame.bfs()

if __name__ == "__main__":
	main()
