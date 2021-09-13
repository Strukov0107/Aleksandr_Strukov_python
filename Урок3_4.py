#3_4
"""Решите систему уравнений:
y = x2 – 1
exp(x) + x(1 – y) = 1
y = x2 – 1
y = (exp(x) + x –  1) / x
"""
import matplotlib.pyplot as plt
import math
import numpy as np

x = np.linspace(-2, 3, 201)

plt.figure(figsize=(6, 12))
plt.plot(x, (np.exp(x) + x - 1) / x)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1, 5)
plt.grid(True)
plt.axis('scaled')
plt.show()

from scipy.optimize import fsolve


def equations(p):
    x, y = p
    return (x ** 2 - 1 - y, np.exp(x) + x * (1 - y) - 1)


x1, y1 = fsolve(equations, (2, 4))
x2, y2 = fsolve(equations, (-1, 1))

print(x1, y1)
print(x2, y2)

"""Решите систему уравнений и неравенств:
y = x2 – 1
exp(x) + x * (1 – y) > 1

y = x2 – 1
y = -1/x +2
"""
from scipy.optimize import fsolve

x = np.linspace(-2, 3, 201)

plt.figure(figsize=(6, 12))
plt.plot(x, (- 1 / x) + 2)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1, 5)
plt.grid(True)

plt.show()


def equations(p):
    x, y = p
    return (x ** 2 - 1 - y, (- 1 / x) + 2 - y)


x1, y1 = fsolve(equations, (2, 4))
x2, y2 = fsolve(equations, (0.5, 0.5))
x3, y3 = fsolve(equations, (-1, 1))

print(x1, y1)
print(x2, y2)
print(x3, y3)

