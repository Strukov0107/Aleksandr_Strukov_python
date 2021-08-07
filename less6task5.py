# задание 5


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашём')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером.')


gel_pen = Pen('Гелевая ручка')

brown_pencil = Pencil('коричневый карандаш')

my_handle = Handle('Мой маркер')

gel_pen.draw()
brown_pencil.draw()
my_handle.draw()