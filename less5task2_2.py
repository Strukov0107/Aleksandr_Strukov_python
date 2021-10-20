#   Задание №2_2 для 5 урока
#   Сгенерируйте десять выборок случайных чисел х0, …, х9
#   и постройте гистограмму распределения случайной суммы  +х0+ …+ х 9

import numpy as np
import matplotlib.pyplot as plt


a = []      #   a   - список 10 случайных чисел
b = []      #   b - сумма чисел списка a
for i in range(10):
    a = np.random.rand(10)
    b.append (sum(a))

print (b)

num_bins = 5
n, bins, patches = plt.hist(b, num_bins)
plt.xlabel('X')
plt.ylabel('Probability')
plt.title('Histogram')