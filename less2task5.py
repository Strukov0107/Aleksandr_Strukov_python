#задание №5

my_list = [7, 5, 3, 3, 2]     #задаём начальный список
print("начальный список :  ", my_list)
print('для выхода из программы введите 666 ')

pos = 0       #введём номер позиции в списке, куда будем добавлять новые цифры

s = True      #зададим условие для  бесконечного цикла
while s == True :
  new_digit = int(input('введите целое однозначное число: '))

  if new_digit == 666:  #условия для входа из программы
     print('Выход')
     break

  counter =0
  for el in my_list:        #сравниваем введённую цифру со всеми цифрами списка по порядку
    lead_dig = my_list[counter]

    if lead_dig < new_digit :     #если новая цифра больше текущей, то вставляем новую цифру в список
      pos = counter
      my_list.insert(pos, new_digit)
      break

    counter = counter +1
    if counter == len(my_list):     #если дошли до конца списка и условия не выполнились, то добавляем новую цифру в конец списка
      pos = counter+1
      my_list.insert(pos, new_digit)
      break

  print (my_list)     #печатаем новый изменённый список