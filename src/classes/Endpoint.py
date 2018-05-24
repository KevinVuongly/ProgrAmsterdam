from algorithms.random import Random

class EndPoint:
    def __init__(self, board, archive, save):
        self.board = board
        self.archive = archive
        self.save = save

    def findEndPoint(self):
        """ Looks for an endpoint in the solution folder. If there is no endpoint found,
            creates a new endpoint through the random algorithm.
        """
        
        try:
            print()
            print("Trying to find the file containing the endpoint... ")

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
