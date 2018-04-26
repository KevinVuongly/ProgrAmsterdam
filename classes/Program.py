from Board import Board
from ReadBoard import ReadBoard

data = ReadBoard("../data/game1.csv")
game = Board(data.gridSize, data.changeable, data.fixed, data.direction, data.length)
