#УРОК 2 ЗАДАНИЕ 3. Нарисовать графики
import matplotlib.pyplot as plt
import math
import numpy as np

#построение окружности
#задаём начальные условия
x_0 = 500  # координата центра окружности
y_0 = 100  # координата центра окружности
r = 200   # радиус окружности

x = []
y = []

lb = x_0 - r     #левая крайняя точка окружности
rb = x_0 + r +1  #правая крайняя точка окружности
for i in range(lb, rb):   #строим верхнюю часть окружности
  x.append(i)
  j = y_0 + ((r**2) - ((i - x_0)**2))**0.5
  y.append(j)

for i in range(lb, rb):   #строим нижнюю часть окружности
  x.append(i)
  j = y_0 - ((r**2) - ((i - x_0)**2))**0.5
  y.append(j)
#построение графика
plt.title('Окружность')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.plot(x,y)
plt.axis('equal')
plt.show()

#построение эллипса
#задаём начальные условия
x_0 = 50  # координата центра эллипса
y_0 = 10  # координата центра эллипса
r_a = 200   # радиус эллипса
r_b = 100   # радиус эллипса

x = []
y = []

lb = x_0 - r_a     #левая крайняя точка эллипса
rb = x_0 + r_a +1  #правая крайняя точка эллипса
for i in range(lb, rb):   #строим верхнюю часть эллипса
  x.append(i)
  j = y_0 + r_b*(1 - ((i - x_0)**2)/(r_a**2))**0.5
  y.append(j)

for i in range(lb, rb):   #строим нижнюю часть эллипса
  x.append(i)
  j = y_0 - r_b*(1 - ((i - x_0)**2)/(r_a**2))**0.5
  y.append(j)
#построение графика
plt.title('Эллипс')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.plot(x,y)
plt.axis('equal')
plt.show()

#построение гиперболы
#задаём начальные условия

a = 2   # параметр гиперболы
b = 4   #  параметр гиперболы
x = []
y = []

for i in range(-20, 20):   #строим верхнюю часть гиперболы
  j = ((a/b*(i**2))-a)**0.5
  y.append(j)
  x.append(i)
for i in range(-20, 20):   #строим верхнюю часть гиперболы
  j = (-1)*((a/b*(i**2))-a)**0.5
  y.append(j)
  x.append(i)

#построение графика
plt.title('Гипербола')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.plot(x,y)
plt.axis('equal')
plt.show()

m = np.linspace(-5, 5,21)
n = 3*m + 1
n2 = (-1/3)*m + 1
plt.title('Параллельные прямые')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.plot (m,n)
plt.plot (m,n2)
plt.axis('equal')

