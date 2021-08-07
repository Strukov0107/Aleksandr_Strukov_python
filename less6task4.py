# задание 4


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, napravlenie):
        if napravlenie == 'left':
            print('машина повернула налево')
        elif napravlenie == 'right':
            print('машина повернула направо')

    def show_speed(self):
        print(f'текущая скорость :  {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('скорость превышена')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('скорость превышена')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


# Проверяем
volga = TownCar(90, "white", 'VOLGA')
print(volga.name)
print(volga.speed)
print(volga.color)
print(volga.is_police)
print(volga.show_speed())
volga.turn('left')

kamaz = WorkCar(80, "red", 'KAMAZ')
print(kamaz.name)
print(kamaz.speed)
print(kamaz.color)
print(kamaz.is_police)
print(kamaz.show_speed())
volga.turn('right')

voronok = PoliceCar(120, 'black', 'Police')
print(voronok.name)
print(voronok.speed)
print(voronok.color)
print(voronok.is_police)
print(voronok.show_speed())
voronok.turn('right')