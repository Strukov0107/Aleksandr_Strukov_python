# задание №6

#with open("test_6.txt", "w") as file:
#    str_list = ['Информатика: 100(л) 50(пр) 20(лаб)\n',
#                'Физика: 30(л) — 10(лаб)\n',
#                'Физкультура: — 30(пр) —\n']           # cоздаём текстовый файл
#    file.writelines(str_list)


result = {}

with open("test_6.txt", "r") as file:
    content = file.readlines()      # считываем содержимое файла

    for el in content:
        str_list = el.split()       # делим строки по пробелу
        name = str_list[0]          # имя предмета
        hours = 0                   # кол-во часов по этому предмету
        num_digit = str(0)          # текущая цифра

        for i in el:
            if i.isdigit():
                num_digit = str(num_digit) + str(i)  # складываем текущие цифры
            else:
                hours = hours + int(num_digit)  # если цифры больше не идут подрял, то переводим в число и прибавляем к часам
                num_digit = 0

        result[name] = hours                    # заносим пару ключ:значение в словарь

print(result)  # печатаем словарь