#   Практическое задание №6_3 для 7 урока
#   Сколько решений имеет линейная система:
#   Если ноль – то измените вектор правой части так, чтобы система стала совместной, и решите ее.

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[12, 2, 1]])
C = np.concatenate((A,B.T), axis=1)
print (C)
np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001)