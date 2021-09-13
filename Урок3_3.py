#3_3
#перевод полярных координат в декартовы
import matplotlib.pyplot as plt
import math
import numpy as np

r = int(input('введите полярные коррдинаты = r'))
phi = int(input('введите полярные коррдинаты = phi'))
def polar2cart(r,phi):
    x = r*math.cos(phi)
    y = r*math.sin(phi)
    return x,y
print (f'декартовы координаты :')
polar2cart(2,45)


#Нарисуйте график окружности в полярных координатах
alfa = np.linspace(0, 2*np.pi, 100)
rad = [10]*len(alfa)
#rad = 8+(alfa*0)
plt.polar(alfa, rad)
plt.show()

#Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах
phi = np.arange(4, 8, 2)
print(phi)
rho = np.arange(4, 8, 2)
print(rho)

plt.polar(phi, rho)
plt.show()



