


class Bfs:
  


    def breadFS(self):
        nodes = []
        beginState = self.changeable
        posMoves = checkPossibleMoves(beginState)

        #Create the first set of children
        for i in range(self.nrOfCars)
            for j rang(len(posMoves[j]))
                child = self.changeable
                child[i] = child[i] + posMoves[i][j]
                explored = []
                queue = [start]
                while true:
                    node = 



