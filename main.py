import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from classes.Board import Board
from classes.ReadBoard import ReadBoard
from algorithms.BFS import BFS

def main(algorithm, data):

	data = "data/game" + data + ".csv"

	beginState = ReadBoard(data)

	if algorithm == "BFS":
		BFS = BFS()
	else:
		raise ValueError("Algorithm not available!")

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])
