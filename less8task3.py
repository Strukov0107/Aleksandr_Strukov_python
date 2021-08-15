# задание №3

class OnlyNums:

    def __init__(self, *digits):
        self.my_list = []

    def input_digits(self):
        print('для остановки цикла введите -  stop  ')
        while True:
            try:
                x = input('ввeдите числo :  ')
                if x == 'stop':
                    print('работа программы завершена ')
                    return

                self.my_list.append(int(x))
                print('текущий список: -  ', self.my_list)

            except:
                print('введённые данные не является числом !!!  ')
                print('попробуйте ввести число или выйдите по команде stop ')


proverka = OnlyNums()
print(proverka.input_digits())













