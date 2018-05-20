"""

x = [10,22,23,45,123,545,76698,323,5475,86,4543,3,576,866,4323,356,67,6744]


x[0:10] = [1,2]
print(x)

for i in range(0,10):
	print(i)

"""
x = []

for i in range(0,123):
	x.append(i)

print(x)
print(len(x))

stepSize = 12
pathLength = len(x)
nrOfsteps = int(pathLength/stepSize)
lastStep = pathLength%stepSize

for i in range(0,nrOfsteps):
	startingState = x[(pathLength - (i+1)*stepSize -1)]
	endBoardstate = x[(pathLength - i*stepSize) - 1]
	y = x[startingState]
	z = x[endBoardstate]
	print(" beginning x = {}, ending x = {}".format(y,z))

if lastStep != 0:
	startingState = x[0]
	endBoardstate = x[(lastStep -1)]
	y = x[startingState]
	z = x[endBoardstate]
	print(" beginning x = {}, ending x = {}".format(y,z))

