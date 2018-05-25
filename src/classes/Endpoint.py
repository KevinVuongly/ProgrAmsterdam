from algorithms.random import Random
import ast

class EndPoint:
    """ Class containing the creation of an endpoint(if needed). """
    def __init__(self, board, archive, save):
        """ Takes all information of the board with it's state as the beginning of the game.

            Args:
                board (class): Containing all information of the game.
                archive (class): Containing the archive class.
                save (class): Containing the save class.
        """
        self.board = board
        self.archive = archive
        self.save = save

    def findEndPoint(self):
        """ Looks for an endpoint in the solution folder. If there is no endpoint found,
            creates a new endpoint through the random algorithm.

        Return:
            solutionState (list): The referred endpoint.
        """

        try:
            print()
            print("Trying to find the file containing the endpoint in solutions/endSolution/..  ...")

            with open(self.save.endStateFolder + str(self.save.gameNumber) + ".txt", "r") as textfile:
        	    solutionState = textfile.readline()
            solutionState = ast.literal_eval(solutionState)

            print("Endpoint found!")
            print()
        except:
            print("Endpoint not found! Creating solution by running the random algorithm...")
            print()

            random = Random(self.board, self.archive, self.save)
            solutionState = random.semiRandomSelection()

            print()
            print("Endpoint created! Ready for the algorithm.")
            print()

        return solutionState
