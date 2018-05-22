"""

x = [10,22,23,45,123,545,76698,323,5475,86,4543,3,576,866,4323,356,67,6744]


x[0:10] = [1,2]
print(x)

for i in range(0,10):
	print(i)

"""
x = []

for i in range(0,124):
	x.append(i)

print(x)
print(len(x))

stepSize = 5
jumps = stepSize + 1 #take one extra, to avoid using same ones twices
pathLength = len(x) 
nrOfsteps = int(pathLength/jumps)
lastStep = pathLength%jumps
print(lastStep)
start = 1
end = 1 + stepSize

#van rechts af

for i in range(0,nrOfsteps):
	startingState = x[-start]
	endBoardstate = x[-end]
	choice = pathLength - (i+1)*stepSize -1
	y = x[startingState]
	z = x[endBoardstate]
	start = end + 1
	end = start + stepSize
	print(" beginning x = {}, ending x = {}".format(y,z))
if lastStep != 0 and (lastStep -1) != 0:       # if laststep -1 is zero it will go from 0 to 0
	start = 0
	end = lastStep - 1
	startingState = x[start]
	endBoardstate = x[end]
	choice = pathLength - (i+1)*stepSize -1
	y = x[startingState]
	z = x[endBoardstate]
	print(" beginning x = {}, ending x = {}".format(y,z))

# van links af
"""
for i in range(0,nrOfsteps):
	print("start = {}, end = {}".format(start, end))
	startingState = x[start]
	endBoardstate = x[end]
	choice = pathLength - (i+1)*stepSize -1
	y = x[startingState]
	z = x[endBoardstate]
	start = end + 1
	end = start + stepSize
if lastStep != 0 and (lastStep -1) != 0:       # if laststep -1 is zero it will bfs from 0 to 0
	start = -lastStep
	end = -1 
	startingState = x[start]
	endBoardstate = x[end]
	choice = pathLength - (i+1)*stepSize -1
	y = x[startingState]
	z = x[endBoardstate]
	print(" start= {}, end = {}".format(y,z))
"""

