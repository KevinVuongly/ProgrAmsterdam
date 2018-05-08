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
			if data < 1 or data > 7:
				print("Please pick an existing game.")
			else:
				break

	while True:
		algorithm = input("Pick which algorithm you want to use(random, BFS): ")
		if algorithm != "random" and algorithm != "BFS":
			print("Please pick a correct algorithm.")
		else:
			data = "data/game" + str(data) + ".csv"

			beginState = ReadBoard(data)

			game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)

			break

	if algorithm == "random":
		random = Random(game)
		radom2 = Random(game)

		solvedgame = random.semiRandomSelection()
		solvedgame2 = random.randomSelection()
		print("length of path {}".format(len(solvedgame)))





	elif algorithm == "BFS":
		bfs = BFS(game)
		bfs.bfs()

if __name__ == "__main__":
	main()
