# задание №3


class Kletka:
    def __init__(self, quant):
        self.quant = quant

    def __add__(self, kletka_2):
        return (self.quant + kletka_2.quant)

    def __sub__(self, kletka_2):
        x = self.quant - kletka_2.quant
        if x > 0:
            return x
        else:
            print('ошибка деления')

    def __mul__(self, kletka_2):
        return (self.quant * kletka_2.quant)

    def __truediv__(self, kletka_2):
        return (self.quant // kletka_2.quant)

    def make_order(self, n):
        count = 0
        for i in range(self.quant):
            if count < n:
                print('#', end=' ')
                count += 1
            else:
                print('')
                print('#', end=' ')
                count = 1
        print(' ')


kletka_1 = Kletka(150)
kletka_2 = Kletka(50)

print(kletka_1 + kletka_2)
print(kletka_1 - kletka_2)
print(kletka_1 * kletka_2)
print(kletka_1 / kletka_2)

kletka_1.make_order(11)

kletka_2.make_order(7)



















