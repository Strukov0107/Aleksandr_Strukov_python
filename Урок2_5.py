#2_5 Построить две параллельные плоскости
# построить две трёхмерные фигуры второго порядка

import numpy as np
import matplotlib.pyplot as plt

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)

X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)

Z = 5*X + 2*Y
ax.plot_wireframe(X, Y, Z)

Z = 5*X + 2*Y +50
ax.plot_wireframe(X, Y, Z)



fig = figure()
ax = Axes3D(fig)
X = np.arange(-1000, 1000, 0.5)
Y = np.arange(-1000, 1000, 0.5)
X, Y = np.meshgrid(X, Y)

Z = (500*(X**2) + 500*(Y**2))**0.5
ax.plot_wireframe(X, Y, Z)

Z = 20000 - (500*(X**2) + 500*Y)**0.5
ax.plot_wireframe(X, Y, Z)
