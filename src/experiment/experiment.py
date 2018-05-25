import time

from classes.Board import Board
from classes.ReadBoard import ReadBoard
from classes.Archive import Archive
from classes.Heuristics import Heuristic
from classes.Save import Save
from algorithms.random import Random
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.astar import Astar
from copy import copy, deepcopy
from classes.Pick import *

def main():

	game = Pick()
	gameNumber = game.pickGame()

	file = "data/game" + str(gameNumber) + ".csv"
	beginState = ReadBoard(file)
	game = Board(beginState.gridSize, beginState.changeable, beginState.fixed, beginState.direction, beginState.length)

	heuristic = Heuristic(game)
	archive = Archive(game, heuristic)
	saveFile = Save(gameNumber, game, archive, beginState.colors)

	random = Random(game, archive)
	
	solutions = []

	for i in range(0,3000):
		newGame = deepcopy(random)
		solution = newGame.semiRandomSelection()
		solutions.append(solution)
		print(i)

	saveSolution(solutions, gameNumber)


def saveSolution(solutionState, game):
	textfile = "experiment/game" + str(game) + "simulations.csv"

	with open(textfile, "w") as file:
		for row in solutionState:
			newRow = str(row)
			file.write(newRow)
			file.write('\n')




if __name__ == "__main__":
	main()