# задание №4

class Sklad:
    def __init__(self, stellaj, level, mesto, goods_list):
        self.stellaj = stellaj  # номер стеллажа
        self.level = level  # номер уровня на стеллаже
        self.mesto = mesto  # номер места на уровне
        self.goods_list = good;
        s_list  # список товаров на складе


class Orgtekhnika:
    def __init__(self, name, quant, ex_date, doc_detail):
        self.name = name  # Наименование товара
        self.quant = quant  # Количество товара
        self.ex_date = ex_date  # Срок хранения товара
        self.doc_detail = doc_detail  # Реквизиты документа


class Printer(Orgtekhnika):
    def __init__(self, type_pr, speed_pr, format_pr, lotok_qt):
        self.type_pr = type_pr  # тип принтера
        self.speed_pr = speed_pr  # скорость печати
        self.format_pr = format_pr  # формат печати (А3 и/или А4)
        self.lotok_qt = lotok_qt  # количество лотков


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













