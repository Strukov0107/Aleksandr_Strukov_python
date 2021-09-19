#   Задание №3_1 для 5 урока
#   Дополните код Монте-Карло последовательности независимых испытаний
#   расчетом соответствующих вероятностей (через биномиальное распределение)
#   и сравните результаты.

import numpy as np
import math

k, n = 0, 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k += 1
print('для k=2 и n=4   :')
print('метод монте карло :  ', end=' ')
print(k, n, k/n)
print('биномиальное распределение  :', end=' ')
cnk = math.factorial(4)/(math.factorial(2)*math.factorial(4-2))
p = cnk/(2**4)
print(p)
print()

#   Задание №3_2 для 5 урока
#   то же самое, что и в задании 3_1,
#   но с другими коэффициентами
#   n=5,  k=4

k, n = 0, 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
x = a + b + c + d + e
for i in range(0, n):
    if x[i] == 4:
        k += 1
print('для k=4 и n=5   :')
print('метод монте карло :  ', end=' ')
print(k, n, k/n)
print('биномиальное распределение  :', end=' ')
cnk = math.factorial(5)/(math.factorial(4)*math.factorial(5-4))
p = cnk/(2**5)
print(p)
