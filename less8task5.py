# задание №5

class Sklad:
    def __init__(self, stellaj, level, mesto, goods_list):
        self.stellaj = stellaj  # номер стеллажа
        self.level = level  # номер уровня на стеллаже
        self.mesto = mesto  # номер места на уровне
        self.new_goods_data = new_goods_data  # данные только что поступившего товара


class Orgtekhnika(Sklad):
    def __init__(self, name, quant, ex_date, doc_detail):
        self.name = name  # Наименование товара
        self.quant = quant  # Количество товара
        self.ex_date = ex_date  # Срок хранения товара
        self.doc_detail = doc_detail  # Реквизиты документа

    def posting(self):  # размещение товара на складе
        self.goods_list = []  # список всех товаров на складе
        while True:
            try:
                print('введите данные для поступившего на склад товара:  ')
                new_name = input('Наименование товара : ')
                new_quant = input('Количество товара : ')
                new_ex_date = input('Срок хранения товара : ')
                new_doc_detail = input('Реквизиты документа : ')
                new_goods_data = {'Наименование товара : ': new_name,
                                  'Количество товара : ': new_quant,
                                  'Срок хранения товара : ': new_ex_date,
                                  'Реквизиты документа : ': new_doc_detail,
                                  }
                self.new_goods_data = new_goods_data
                self.goods_list.append(new_goods_data)
                print(f'на склад приходовано следующее оборудование :  ', new_goods_data)
                q = input(f'Для выхода - Q, продолжение - Enter')
                if q == 'Q' or q == 'q':
                    print(f'Весь склад -\n {self.goods_list}')
                    return f'Выход'
                else:
                    return Orgtekhnika.posting()
            except:
                print('Ошибка ввода данных: ')


class Printer(Orgtekhnika):
    def __init__(self, type_pr, speed_pr, format_pr):
        self.type_pr = type_pr  # тип принтера
        self.speed_pr = speed_pr  # скорость печати
        self.format_pr = format_pr  # формат печати (А3 и/или А4)


class Scanner(Orgtekhnika):
    def __init__(self, resolution, color_deep, speed_sc):
        self.resolution = resolution  # оптическое разрешение
        self.color_deep = color_deep  # глубина цвета
        self.speed_sc = speed_sc  # скорость сканирования


class Xerox(Orgtekhnika):
    def __init__(self, format_xr, speed_xr, resurs_xr):
        self.format_xr = format_xr  # формат бумаги
        self.speed_xr = speed_xr  # скорость копирования
        self.resurs_xr = resurs_xr  # ресурс аппарата


printer_1 = Printer('canon', 300, 'A4')
printer_1.posting()











