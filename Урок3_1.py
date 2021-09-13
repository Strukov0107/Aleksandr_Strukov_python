#3_1
# построение графика функции
import matplotlib.pyplot as plt
import math
import numpy as np

# построение графика функции
# задаём начальные условия
a = 3.14  #
b = 1  #
k = 10  #

x = np.linspace(-2 * np.pi, 5 * np.pi, 202)
plt.plot(x, k * np.cos(x - a) + b)
plt.title('k*COS(x-a)+b')

x = np.linspace(-2 * np.pi, 5 * np.pi, 202)
plt.plot(x, 3 * np.cos(x - 1.5 * a) + 6)

x = np.linspace(-2 * np.pi, 5 * np.pi, 202)
plt.plot(x, 6.5 * np.cos(x - 0.75 * a) + 2)

plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()







