
from classes.ReadBoard import ReadBoard
from classes.Pick import *
import numpy


def main():

	game = Pick()
	gameNumber = game.pickGame()


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
	x = 1
	for element in array:
		x = x*element

	return x




def statesInGrid(carsSpaces):
	states = []
	for rowCollumn in carsSpaces:
		state = statesPerRowCollumn(rowCollumn)
		states.append(state)

	return states 



def statesPerRowCollumn(carsSpaces):
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



