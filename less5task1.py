# задание №1

file = open("test.txt", "w")                     # создаём файл


str_list = input('введите строку текста: ')  # пользователь вводит текст

while str_list:  # цикл
    file.write(str_list + '\n')                  # записываем строку в файл
    str_list = input('введите строку текста: ')  # пользователь вводит текст

file.close()  # закрываем файл

file = open("test.txt", "r")                     # блок для печати файла
content = file.read()
print(content)
file.close()