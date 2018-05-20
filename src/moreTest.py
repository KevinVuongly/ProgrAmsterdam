import time

import csv

from classes.ReadStates import ReadStates
from classes.Board import Board
from classes.ReadBoard import ReadBoard
from classes.Archive import Archive
from classes.Heuristics import Heuristic
from algorithms.random import Random
from algorithms.bfsBetweenStates import BFSBetweenStates
from algorithms.dfs import DFS
from copy import copy, deepcopy
from algorithms.IterativeSegmentBfs.py import *

def main():

	henk = IterativeBfs()
	henk.iterativeBfs(2,3,15)

if __name__ == "__main__":
	main()