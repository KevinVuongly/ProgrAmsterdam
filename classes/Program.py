from Board import Board
from ReadBoard import ReadBoard

data = ReadBoard("../data/game1.csv")
game = Board(data.gridSize, data.changeable, data.fixed, data.direction, data.length)

<<<<<<< HEAD
game.visualize(data.changeable, data.colors)
=======
game.checkPossibleMoves()

>>>>>>> e3d872d528bcb10c154a204ed2e64facdca8e164
