#   Задание №4 для 4 урока
#   Sin(a*x)=0   0.01<a<0.02   100<x<500
#   x=f(a) -?


import numpy as np
import matplotlib.pyplot as plt
import math

#   Sin(a*x)=0
#   a*x=п*К, где К принадлежит Z
#   x=(п/a)*K

a_0 = 0.01        #начальное условие
a_k = 0.02        #конечное условие
step = 0.0001     #шаг
a = a_0           #начальное условие

k_0 = int(100 // (np.pi / a))
X = []
A = []

while a <= a_k:
  k_0 = int(100 // (np.pi / a))
  k_0 +=1
  x = round((np.pi / a) *k_0, 4)
  while x <= 500:
    X.append(x)
    A.append(a)
    k_0 +=1
    x = round((np.pi / a) *k_0, 4)
  a = round(a+step, 5)


#построение графика
plt.title('график x=F(a)')
plt.xlabel('A')
plt.ylabel('X')
plt.grid()
plt.scatter(A, X, color='r')

#распечатка данных
print (A)
print (X)

