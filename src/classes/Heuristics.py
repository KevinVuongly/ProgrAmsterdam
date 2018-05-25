from classes.Board import Board

class Heuristic:
    """ A class that has all the heuristics made for the rush hour game"""

    def __init__(self, board):
        """ Takes all information of the board with it's state as the beginning of the game.

        Args:
            board (class): Containing all information of the game.
        """

        self.board = board

    def blockingRedCar(self, stateChangeable):
        """ Checks how many cars are blocking the way of the red car.

        Initalization:
            blocks (int): Amount of blocks is 0 initially.
            redCarSize (int): The carsize of the red car. The size is typically 2.
            posToCheck (int): The maximum amount of cars that might be
                              blocking the way of the red car.

        Args:
            stateChangeable (list): The current state of the game.

        Return:
            blocks (int): The real amount of cars blocking the way of the red car.
        """
        blocks = 0
        redCarSize = self.board.length[0]

        posToCheck = self.board.gridSize - stateChangeable[0] - redCarSize

        for i in range(1, self.board.nrOfCars):
            if self.board.direction[i] == "v":
                for j in range(posToCheck):
                    for k in range(self.board.length[i]):
                        if stateChangeable[i] == self.board.fixed[0] - k and self.board.fixed[i] == redCarSize + stateChangeable[0] + j:
                            blocks += 1
                            break

        return blocks

    def positionScore(self, stateChangeable, stateSolution):
        """ Calculates the score of the given board compared to the solution board.
            For every distance difference of a car compared to it's position in
            the solution adds a penalty of 1.

        Args:
            stateChangeable (list): The current state of the game.
            stateSolution (list): The solution state of the game.

        Return:
            score (int): The score of the given board according to the heuristic.
        """
        score = 0

        for i in range(self.board.nrOfCars):
            score += abs(stateSolution[i] - stateChangeable[i])

        return score
