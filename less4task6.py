# задание №6

from itertools import count       #импортируем модули
from itertools import cycle

#part A                           #задание А
start_dig = int (input ('введите число, c которого формировать список: '))

for el in count(start_dig):       #формируем список
    if el > 15:
        break
    else:
        print(el)

#part B                           #задание В
my_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  #наш список

сounter = 0
stop_dig = int (input ('введите число, когда заканчивать список'))

for el in cycle(my_list):         #зацикливаем список
    if сounter > stop_dig:
        break
    print(el)
    сounter += 1