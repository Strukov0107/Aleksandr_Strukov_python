#задание №7

class MyComplex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'c + d * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'

    def __add__(self, other):
        c = self.a + other.a
        d = self.b + other.b
        print(f'Сумма z1 и z2 равна')
        return f'z = {c} + {d} * i'

    def __mul__(self, other):
        c = (self.a * other.a) - (self.b * other.b)
        d = (self.b * other.a) + (self.a * other.b)
        print(f'Произведение z1 и z2 равно')
        return f'z = {c} + {d} * i'



z_1 = MyComplex(5, -6)
z_2 = MyComplex(7, 8)

print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)