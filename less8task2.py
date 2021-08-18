# задание №2

class MyError:

    @staticmethod
    def delenie(a, b):
        try:
            return (a / b)
        except:
            return ("Деление на ноль недопустимо")


print(MyError.delenie(23, 0))
print(MyError.delenie(10, 0))
print(MyError.delenie(10, 0.1))
print(MyError.delenie(100, 0))













