# ProgrAmsterdam - Rush Hour
To get a better understanding of how the classes are used, please check each file in the following order:

- ReadBoard: Reads the csv-file containing a given game. It basically creates the game.
- Board: Contains actions to move the board e.g. creating the children of the board
         and a check if the board is solved.
- Archive: Contains the archive and actions to update the archive.
- Heuristics: Contains the heuristics used in the solver.
- Endpoint: Contains a function to find an endpoint. If it doesn't exist, creates one through
            the random algorithm. This is needed for a heuristic that is used in the solver.
- Save: Saves the solution found through the solver.
- ReadStates: Reads the csv-file created in the Save class. Used for an experiment.
              This class is not implemented in the solver itself.
