import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from classes.Board import Board
from classes.ReadBoard import ReadBoard
from algorithms.BFS import BFS

def main():

	while True:
		data = input("Pick the game you want to solve for (1, 2, 3,..., 7): ")

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
		algorithm = input("Pick which algorithm you want to use(BFS): ")
		if algorithm != "BFS":
			print("Please pick a correct algorithm.")
		else:
			break

	data = "data/game" + str(data) + ".csv"

	beginState = ReadBoard(data)

	game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)

	game.visualize(beginState.changeable, beginState.colors)

	if algorithm == "BFS":
		print("correct")
	else:
		raise ValueError("Algorithm not available!")

if __name__ == "__main__":
	main()
