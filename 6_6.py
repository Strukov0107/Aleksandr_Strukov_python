#   Практическое задание №6_6 для 7 урока
#   Найдите одно из псевдорешений вырожденной системы:
#   Попробуйте также отыскать и нормальное псевдорешение.

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([2, 5, 11])
Q, R = np.linalg.qr(A)

print(A)
print(Q)
print(R)
print()

print(np.dot(Q, R))
print(np.dot(np.transpose(Q), Q))
print()

R1 = R[:2, :2]
R1
print()

B1 = np.dot(np.transpose(Q), B)[:2]
B1
print()

X1 = np.linalg.solve(R1, B1)
X1
print()

X = np.append(X1, 0)
print(X)
np.linalg.norm(X)
print()

np.linalg.norm(np.dot(A, X) - B)
print()

X = np.array([1.5, 1, 0.5])
np.linalg.norm(X), np.linalg.norm(np.dot(A, X) - B)
