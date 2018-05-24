from classes.ReadStates import ReadStates

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
import scipy.stats

file = "experiment/game3simulations.csv"
stat = ReadStates(file)
x = stat.readStates()
y = []
for [jokem] in x:
	y.append(jokem)

ks_results = scipy.stats.kstest(y, cdf='norm')

matrix_ks = [
    ['', 'DF', 'Test Statistic', 'p-value'],
    ['Sample Data', len(y) - 1, ks_results[0], ks_results[1]]
]

ks_table = FF.create_table(matrix_ks, index=True)
py.iplot(ks_table, filename='ks-table')

"""
num_bins = 10
n, bins, patches = plt.hist(y, num_bins, normed=1, facecolor='blue', alpha=0.5)
plt.title(r'Histogram of nr of moves for solution random algorithm: game 3')
plt.show()


file = "experiment/game2simulations.csv"
stat = ReadStates(file)
x = stat.readStates()
y = []
for [jokem] in x:
	y.append(jokem)

num_bins = 10
n, bins, patches = plt.hist(y, num_bins, normed=1, facecolor='blue', alpha=0.5)
plt.title(r'Histogram of nr of moves for solution random algorithm: game 2')
plt.show()
"""