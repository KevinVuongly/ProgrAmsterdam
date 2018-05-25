
from classes.ReadBoard import ReadBoard
from classes.Pick import *
import numpy


def main():

	game = Pick()
	gameNumber = game.pickGame() # Choose game


	file = "data/game" + str(gameNumber) + ".csv"
	beginState = ReadBoard(file)

	carsSpacesRows = spacesCars("h", beginState)		# get nr of free spaces and nr of cars for each row
	carsSpacesCollumns = spacesCars("v", beginState)	# get nr of free spaces and nr of cars for each collumn 

	statesPerRow = statesInGrid(carsSpacesRows)         # get nr of state for each row
	statesPerCollumn = statesInGrid(carsSpacesCollumns) # get nr of states for each collumn

	horizontalStates = product(statesPerRow)
	verticalStates = product(statesPerCollumn)
	states = horizontalStates * verticalStates

	print("The maximum statespace for game {} is {} spaces".format(gameNumber,states))

def product(array):
	""" Multiplies all elements in an array """ 
	x = 1
	for element in array:
		x = x*element

	return x




def statesInGrid(carsSpaces):
	""" makes an array of the nr of states per collumn or row """
	states = []
	for rowCollumn in carsSpaces:
		state = statesPerRowCollumn(rowCollumn)
		states.append(state)

	return states 



def statesPerRowCollumn(carsSpaces):
	""" Calcutates the nr of states for a row or a collunn """
	nrOfCars = carsSpaces[0]
	freeSpaces = carsSpaces[1]
	y = [freeSpaces]
	for i in range(nrOfCars):
		x = []
		for element in y:
			while element >= 0:
				x.append(element)
				element -= 1
		y = x
	return len(y)



def spacesCars(direction, beginState):
    """ Counts how many cars occupy a row or a collumn and calculates the free spaces in the row or collumn

    Args:
        direction (string): containing if you want to search a row or a collumn
        beginstate (list): Containing the board state

    Return:
    	carsSpaces (list): A list with the amount of cars and the free spaces per row or collumn
    """
	carsSpaces = []
	for i in range(beginState.gridSize):        # check per row
		cars = 0
		freeSpaces = beginState.gridSize
		for j in range(len(beginState.changeable)):      
			if beginState.fixed[j] == i and beginState.direction[j] == direction:   # Check if car is horizontal in that row
				cars += 1
				freeSpaces -= beginState.length[j]               # decrease freeSpaces bij carlength
		carsSpaces.append([cars, freeSpaces])

	return carsSpaces

if __name__ == "__main__":
	main()



