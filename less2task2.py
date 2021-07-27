#задание №2
spisok = []   #создаём пустой список
l = int (input ('Введите желаемую длинну списка: '))#запрашиваем длинну списка
count = 0     #сбрасываем счётчик

while count < l :
  print ('Введите элемент списка № ', count, end=',это будет  ')  #просим ввести элемент списка
  spisok.append(input())                  #добавляем элемент списка
  count = count +1
print ("список до замены   ", spisok)     #печатаем список

count = 0   #обнуляем счётчик

while (l-count) > 1:   #организуем цикл
  spisok[count], spisok[count+1]=spisok[count+1], spisok[count] #меняем значения попарно
  count = count + 2
print ("список после замены", spisok)     #печатаем новый список
