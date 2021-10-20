#   Задание №4 для 5 урока
#   повторим расчеты,
#   сгенерировав возможные варианты перестановок для других значений n и k
#   n=10, k=1,2,3,4,5,6,7,8,9,10


import numpy as np
import math


k, n = 0, 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
f = np.random.randint(0, 2, n)
g = np.random.randint(0, 2, n)
h = np.random.randint(0, 2, n)
r = np.random.randint(0, 2, n)
t = np.random.randint(0, 2, n)
x = a + b + c + d + e +f + g + h +r + t

for j in range(1,10):
    k = 0
    for i in range(0, n):
        if x[i] == j:
            k += 1
    print(f'для k={j} и n=10   :')
    print('метод монте карло :  ', end=' ')
    print(k, n, k/n)
    print('биномиальное распределение  :', end=' ')
    cnk = math.factorial(10)/(math.factorial(j)*math.factorial(10-j))
    p = cnk/(2**10)
    print(p)
    print()