print ('Задание №1')  #задание №1
chislo_1= int(input('Введите первое число '))
chislo_2= int(input('Введите второе число '))
chislo_3= int(input('Введите третье число '))
stroka_1= input('Введите первую строку ')
stroka_2= input('Введите вторую строку ')
stroka_3= input('Введите третью строку ')
print ('Сложим ваши цифры:', chislo_1 + chislo_2 + chislo_3)  #Числа должны сложиться
print ('Сложим ваши строки:', stroka_1 + stroka_2 + stroka_3) #Строки должны идти друг за другом

print ('Задание №2')  #задание №2
vremya=int(input('Введите время в секундах: ')) #вводим время в секундах
chasy=int(vremya//3600)         #вычисляем количество полных часов
minuty_sec=int(vremya%3600)     #остаток от полных часов
minuty=int(minuty_sec//60)      #вычисляем минуты
sec=int(minuty_sec%60)          #вычисляем секунды
print('Часы',chasy)
print('Минуты',minuty)
print('Секунды',sec)
print('Московское время: ', chasy, ':', minuty, ':', sec)  #печатаем результат в нужном формате

print ('Задание №3') #задание №3
n=int(input('Введите целое положительное число:'))
summ=n+(n*10+n)+(n*100+n*10+n)          #Вычисляем сумму
print(n,'+',n,n,'+', n,n,n,'=',summ)    #выводим на печать

print ('Задание №4')#задание  №4
n=str(input('Введите целое положительное число:'))
dlinna=len(n)      #определяем длинну числа
counter=0          #обнуляем счётчик циклов
maximum=n[0]       #вводим переменную- максимальное число на данном этапе цикла
while counter<dlinna:     #цикл сравнения всех цифр в числе
  if maximum<n[counter]:
    maximum=n[counter]
  counter+=1
print('Максимальная цифра =',maximum)

print ('Задание №5')   #задание №5
viruchka=float(input('Введите размер выручки:'))
izderjki=int(input('Введите размер издержек'))

if viruchka>izderjki:
  print('Фирма получила прибыль')
  print('Вычисляем рентабельность')
  n=int(input('Введите численность персонала'))
  rentabelnost=(viruchka-izderjki)/n
  print('Рентабельность проекта составила =',rentabelnost)

if viruchka<izderjki:
  print('Фирма получила убытки')

if viruchka==izderjki:
  print('Фирма сработала в ноль')

print ('Задание №6')   #задание №6
pervyi_den=float(input('Сколько километров пробежал спортсмен в первый день:'))
konechyi_rezultat=float(input('Какой нужен конечный результат: '))
n=1                     #счётчик количества дней
probeg=pervyi_den       #Сколько пробежал в этот день

while probeg<konechyi_rezultat:   #вычисляем пробег по дням
  probeg*=1.1
  n+=1
  print(n,"День. Пробег составил",probeg)

print('Потребовалось',n ,'Дней')   #печатаем результат