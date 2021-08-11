# задание №7

import json

companies = {}

good_company = 0  # успешные компании
many_company = 0  # прибыль компаний

with open("test_7.txt", "r") as file:
    content = file.readlines()  # считываем содержимое файла

    for el in content:
        str_list = el.split()  # делим строки по пробелу
        money = float(str_list[2]) - float(str_list[3])
        name = str_list[0]  # имя
        companies[name] = money

        if money > 0:
            good_company += 1
            many_company += money

sred_pribil = many_company / good_company

spisok = [companies, {'srednaya_pribil': sred_pribil}]

with open("spisok.json", "w") as file:
    json.dump(spisok, file)