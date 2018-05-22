class Astar:
    def __init__(self, board, archive):
        """
        Takes all information of the board with it's state as the beginning of the game.
        """
        self.board = board

        self.archive = archive
        self.archive.visitedStates[str(self.board.changeable)] = "beginning!"

    def astar(self, save):
        """ Runs A*-search on the initialized board.
        
        The algorithm stops when it finds a solution e.g. a state which the red car can move to the end.
        """
        self.save = save
