# задание №4

spisok = input("Введите несколько слов, разделённых пробелами ")  # вводим список

spisok_2 = spisok.split()  # разделяем строку по пробелам на несколько элементов. заносим во второй список

counter = 0          # обнуляем счётчик
for el in spisok_2:  # проходим по всем элементам второго списка
    s = spisok_2[counter]  # выделяем текущий элемент списка
    srez = s[:10]          # делаем срез по первым 10 символам
    print("строка номер: ", counter + 1, " -  ", srez)  # печатаем порядковый номер и срез текущего элемента списка
    counter = counter + 1  # увеличиваем счётчик на 1
