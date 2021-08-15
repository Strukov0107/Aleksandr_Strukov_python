# задание №1
import random


class Matrix:

    def __init__(self, matrix):  # kolonki -кол-во колонок; stroki - кол-во строк
        self.matrix = matrix

    def __str__(self):  # вывод на печать в виде матрицы
        matr_print = ""  # пустая матрица
        for i in range(len(self.matrix)):  # прибавляем элемены из матрицы + пробел
            for j in range(len(self.matrix[i])):
                matr_print = matr_print + str(self.matrix[i][j]) + " "
            matr_print = matr_print + "\n"  # переход на след строку
        return matr_print

    def __add__(self, matrix_plus):
        summa_matrix = ""                   # пустая матрицакуда запишем сумму матриц
        for i in range(len(self.matrix)):   # прибавляем элемены из матрицы + пробел
            for j in range(len(self.matrix[i])):
                x = int(self.matrix[i][j]) + int(
                    matrix_plus.matrix[i][j])               # складываем два элемента матрицы алгебраически
                summa_matrix = summa_matrix + str(x) + " "  # добавляем сумму в строку + пробел
            summa_matrix = summa_matrix + "\n"  # переход на след строку
        return summa_matrix


# создадим две матрицы размером 7 на 5
stroki = 5   # stroki - кол-во строк
kolonki = 7  # kolonki -кол-во колонок
matrix_1 = Matrix([[random.randrange(0, 10) for a in range(kolonki)] for b in range(stroki)])
matrix_2 = Matrix([[random.randrange(0, 10) for a in range(kolonki)] for b in range(stroki)])

# напечатем две матрицы
print('матрица №1 :  ')
print(matrix_1)
print('матрица №2 :  ')
print(matrix_2)

# сложим две матрицы
print(matrix_1 + matrix_2)
























