# задание 1

import time


class TrafficLight:  # класс светофоры
    color = 'red'  # атрибут - цвет

    def __init__(self):  # конструктор
        self.__color = 'green'  # атрибут private

    def running(self):  # метод
        while True:
            print('red')
            time.sleep(7)
            print('yellow')
            time.sleep(2)
            print('green')
            time.sleep(7)


svetofor_1 = TrafficLight()  # объект класса светофоры

svetofor_1.running()  # обращаемся к методу