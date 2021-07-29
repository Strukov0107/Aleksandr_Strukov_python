# задание №5

from functools import reduce                             #импортируем модули

my_list = [x for x in range(100, 1001) if x % 2 == 0]    #создаём список
print (my_list)

def my_funct (el1, el2):                                 #описываем функцию
  return el1 * el2

print (reduce (my_funct, my_list))                       #применяем reduce и печатаем