#задание №4


#file = open ("test_4.txt", "w")
#str_list = ['One — 1\n',
#            'Two — 2\n',
#            'Three — 3\n',
#            'Four — 4\n']                     #cоздаём текстовый файл
#file.writelines(str_list)
#file.close()


file = open ("test_4.txt", "r")
content = file.readlines()                    #считываем содержимое файла
print (' изначальный файл содержит : ', content)
file.close()

#заменяем английские слова на русские         #создаём словарь слов для замены
my_dict = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}

new_file = open ("test_4new.txt", "w")        #открываем изначальный файл
for line in content:                          #проверяем каждую строку
  my_str = line.split(' ')                    #разбиваем строку по пробелу
  for el in my_str:                           #берём каждый элемент
    if el in my_dict:                         #сравниваем со словарём, если совпал, то
      eng_num = el                            #присваиваем значение переменной с английским номером
      rus_num = my_dict.get (el)              #присваиваем значение переменной с русским номером (из словаря)

  new_line = line.replace (eng_num, rus_num)  #заменяем в строке английский номер на русский
  new_file.write (new_line)                   #записываем новую строку в файл
new_file.close()                              #закрываем новый файл

new_file = open ("test_4new.txt", "r")
content = new_file.readlines()                    #считываем содержимое файла
print (' Новый файл содержит :       ', content)
new_file.close()