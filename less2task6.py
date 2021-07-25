#задание №6

slovar_1 = {}               #присваиваем имена словарям
slovar_2 = {}
slovar_3 = {}

kortej_1 = (1, slovar_1)    #присваиваем имена кортежам
kortej_2 = (2, slovar_2)
kortej_3 = (3, slovar_3)

tovary = [kortej_1, kortej_2, kortej_3]   #вводим структуру данных = товары

slovar_key = ['название', 'цена', 'количество', 'единица измерения']    #определяем ключи словарей

#заполняем словари
for number, slovar in tovary:
  print('заполняем словарь № ', number, ': ')
  counter = 0
  while counter < 4:
    task1 = slovar_key[counter]
    print("введите", task1, end=': ')
    task2 = input()
    slovar[task1] = task2
    counter = counter + 1
  print('печатаем словарь № ', number, slovar)
  print(' ')

print('печатаем товары :', tovary)  #выводим на печать всю структуру данных

#собираем аналитику
analitika = {}                        #вводим файл с необходимой аналитикой

for number, slovar in tovary:         #проверяем все кортежи
  for key, value in slovar.items():   #проверяем все словари
    if not analitika.get(key):        #проверяем есть ли такой ключ
      analitika[key] = [value]        #добавляем ключ с элементом в словарь
    else:
      analitika[key].append(value)    #добавляем элемент в словарь к существующему ключу

print ('выводим файл с результатами аналитики :  ', analitika)    #выводим на печать результатalitika)    #выводим на печать результат