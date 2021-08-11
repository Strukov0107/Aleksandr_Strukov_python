# задание №5

import random  # импортируем модули
from random import randint

num_list = [randint(1, 50) for x in range(15)]  # создаём случайную последовательность чисел
my_list = " ".join(map(str, num_list))  # убираем запятые, пишем числа через пробел

with open("test_5.txt", "w") as file:  # cоздаём текстовый файл
    file.write(my_list)  # записываем последовательность в файл

with open("test_5.txt", "r") as file:
    content = file.read()  # считываем содержимое файла

summ = 0
new_list = content.split()  # разделяем последовательность

for x in new_list:  # подсчитываем сумму чисел
    summ = summ + int(x)

print('сумма чисел равна : ', summ)