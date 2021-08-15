# задание №1

class Data:

    def __init__(self, ddmmyy):
        self.ddmmyy = str(ddmmyy)

    @classmethod  # классметод
    def metod_1(cls, ddmmyy):
        int_data = []  # пустой список
        x = ddmmyy.split('-')  # разделяем по пробелу
        for el in x:  # каждый элемент
            int_data.append(int(el))  # переводим в int
        Data.int_data = int_data  # и добавляем в список
        return cls.int_data  # возвращаем дату списком, элементы которого в формате "число"

    @staticmethod  # статикметод
    def metod_2(ddmmyy):  # принимаем дату в формате дд-мм-гг
        x = ddmmyy.split('-')  # разделяем по пробелу
        d = int(x[0])  # переменная день
        m = int(x[1])  # переменная месяц
        y = int(x[2])  # переменная год

        if 0 < d < 32:  # проверяем диапазон дня
            if 0 < m < 13:  # проверяем диапазон месяца
                if 0 < y < 2022:  # проверяем диапазон года
                    print("с датой всё в порядке")
                else:
                    print("год вне диапазона")
            else:
                print("месяц вне диапазона")
        else:
            print("день вне диапазона")


Data.metod_2("11-08-2021")  # проверяемдиапазон день, месяц, год
Data.metod_1("11-08-2021")  # вызываем дату в формате int



















