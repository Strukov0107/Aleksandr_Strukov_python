#   Практическое задание №6_5 для 7 урока
#   Найдите нормальное псевдорешение недоопределенной системы:
#   Для этого определите функцию Q(x,y,z), равную норме решения, и найдите ее минимум.

import numpy as np
import matplotlib.pyplot as plt

def Q(x, y, z):
  return (x**2 + y**2 + z**2)
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, Q(X, 5*X - 14, 21*X - 1))


A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([1, 12])
np.linalg.lstsq(A, B)
