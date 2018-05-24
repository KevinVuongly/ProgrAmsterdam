from classes.ReadStates import ReadStates

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
from classes.Pick import *

import numpy as np
import pandas as pd
import scipy
import scipy.stats


game = Pick
gameNumber = game.PickGame()



file = "experiment/game" + str(gameNumber) + "simulations.csv"
stat = ReadStates(file)
x = stat.readStates()
y = []
for [jokem] in x:
	y.append(jokem)



num_bins = 10
n, bins, patches = plt.hist(y, num_bins, normed=1, facecolor='blue', alpha=0.5)
plt.title(r'Histogram of nr of moves for solution random algorithm: game %i' %gameNumber)
plt.show()


