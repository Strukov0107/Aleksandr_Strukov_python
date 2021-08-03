#задание №1


def my_function (arg1, arg2):

  if arg2 == 0:
    return 'на ноль делить нельзя'

  return arg1 / arg2

print (my_function (float(input('введите первое число : ')),float(input('введите второе число : '))))

