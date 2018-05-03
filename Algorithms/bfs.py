


class Bfs:
    def __init__(self, gridSize, changeable, fixed, direction, length):
        """Initialisation of the board's parameters.

        Args:
            gridSize (int): An integer for the size of the grid.
            changeable (list of ints): An int for the variable position of car i.
            fixed (list of ints): An int for the fixed position of car i.
            direction (list of strings): A character for the direction the car i is facing.
            length (list of ints): The length of car i.
            nrOfCars (int): The number of cars on the grid.
        """

        self.gridSize = gridSize
        self.changeable = changeable
        self.fixed = fixed
        self.direction = direction
        self.length = length
        self.nrOfCars = len(changeable)




    def get_breadth_first_nodes(self):
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




        while stack:
            cur_node = stack[0]
            stack = stack[1:]
            nodes.append(cur_node)
            moves = checkPossibleMoves()
            children 
            for child in cur_node.get_children():
                stack.append(child)
        return nodes


    def checkPossibleMoves(self, changeable):
        """
        Checks all possible moves of a given state.
        """

        if checkSolution == 0:
            return 0
            print("solved")

        possiblemovesarray = []

        for j in range(self.nrOfCars):
            minMaxChange = self.gridSize - self.length[j] + 1
            possibleMoves = []
            for i in range(1,minMaxChange):
                if self.checkMove(j, i) == 0:
                    possibleMoves.append(i)
                else:
                    break
            for i in range(1,minMaxChange):
                if self.checkMove(j, -i) == 0:
                    possibleMoves.append(-i)
                else:
                    break
            possiblemovesarray.append(possibleMoves)

        return possiblemovesarray

    def checkSolution(self, changeable):
        """ Solution if 0 """
        movesToEndblock = self.gridSize - changeable[0] - 2
        if self.checkMove(0,movesToEndblock) == 0:
            return 0
        return 1

    def checkMove(self, vehicle, change, changeable):
        """Checks if the move is feasible.

        Args:
            vehicle (Int): The number of the vehicle that is checked.
            change (Int): The number of places you want the vehicle to move,
                          negative or positive, depending on direction.
        """

        newPos = changeable[vehicle] + change
        if not isinstance(change, int):
            return 1

        if newPos < 0 or newPos > self.gridSize - self.length[vehicle]:
            return 1

        usedElement = [[0 for x in range(self.gridSize)] for y in range(self.gridSize)]

        for i in range(len(self.changeable)):
            for j in range(self.length[i]):
                if self.direction[i] == "h":
                    usedElement[self.fixed[i]][changeable[i] + j] = 1
                else:
                    usedElement[changeable[i] + j][self.fixed[i]] = 1


        if change > 0:
            for i in range(change):
                if self.direction[vehicle] == "h":
                    if usedElement[self.fixed[vehicle]][changeable[vehicle] + self.length[vehicle] + i] == 1:
                        return 1
                else:
                    if usedElement[changeable[vehicle] + self.length[vehicle] + i][self.fixed[vehicle]] == 1:
                        return 1
        else:
            for i in range(abs(change)):
                if self.direction[vehicle] == "h":
                    if usedElement[self.fixed[vehicle]][changeable[vehicle] - 1 - i] == 1:
                        return 1
                else:
                    if usedElement[changeable[vehicle] - 1 - i][self.fixed[vehicle]] == 1:
                        return 1
        return 0



"""
class Bfs()

def get_breadth_first_nodes(Board):
    nodes = []
    stack = [Board]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in cur_node.get_children():
            stack.append(child)
    return nodes




class Node(object):

    def __init__(self, id_):
        self.id = id_
        self.children = []

    def __repr__(self):
        return "Node: [%s]" % self.id

    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children
"""