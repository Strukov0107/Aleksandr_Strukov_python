# задание №3


#file = open("test.txt", "w")           # открываем файл для записи
#
#str_list = ['Антонов 30000\n',
 #           'Брытин 15000\n',
 #           'Лукьянов 40000\n',
#            'Новиков 15000\n']         # cоздаём текстовый файл
#file.writelines(str_list)              # записываем текст в файл
#
#file.close()                           # закрываем файл


file = open("test.txt", "r")        # открываем файл для чтения
count_people = 0                    # счётчик количества людей
count_money = 0                     # счётчик количества денег

print('кто имеет оклад менее 20 000  : ')
for line in file:                   # проходим по всем строкам файла

    lead_str = line.split(' ')      # делим строку по пробелу
    count_people += 1               # считаем людей
    count_money += int(lead_str[1])  # считаем деньги

    if int(lead_str[1]) < 20000:    # находим у кого з.п. ниже 20 000
        print(lead_str[0])

print('средний доход : ', count_money / count_people)  # вычисляем и печатаем средний доход

file.close()                        # закрываем файл