# задание №2

import random                 #импортируем модули
from random import randint

my_list = [randint(1, 300) for x in range(20)]  #создаём случайный список
print ('список случайных чисел: ', my_list)     #печатаем случайный список

new_list = []   #называем новый список

#можно было так:
#counter = 0     #обнуляем счётчик

#while counter < len(my_list) -1 :               #проходим цикл по всем элементам списка
 # if my_list [counter +1] > my_list [counter]:  #если следующий элемент больше предыдущего, то
  #  new_list.append(my_list[counter +1])        #заносим его в новый список
  #counter += 1

#но, так короче
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]

print ('список чисел больше предыдущих', new_list)  #печатаем результатin range(20, 240) if (x % 20 == 0) or (x % 21 == 0)])  # печатаем. всё уместилось в одну строку