# задание 2


class Road:  # класс дорога
    length = 0  # атрибут длинна
    width = 0  # атрибут ширина
    massa = 0  # атрибут масса асфальта

    def __init__(self, length, width):  # конструктор
        self._length = length  # атрибут длинна защищённый
        self._width = width  # атрибут ширина защищённый

    def massa_asfalt(self, tolchina, plotnost):  # метод
        # massa = length * width * tolchina * plotnost    -формула для расчёта массы асфальта
        massa = self._length * self._width * (tolchina * 0.01) * (plotnost * 100)  # расчитываем массу
        print(massa)


strasse_1 = Road(1000, 5)  # объект класса (передаём длинну и ширину объекта)

strasse_1.massa_asfalt(5, 25)  # обращаемся к методу (передаём толщину в cм и плотность в тонн/м3)