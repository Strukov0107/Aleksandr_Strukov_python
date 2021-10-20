#   Задание №1 для 5 урока
#   написать код, моделирующий
#   выпадение чисел в рулетке


import numpy as np

while True:
    print ('делайте ваши ставки.  Для остановки введите stop')
    vvod = input ('введите число от 1 до 36   - ')
    if vvod == 'stop':
        print('программа остановлена')
        break
    st = int (vvod)
    print (f'ваша ставка - {st}')

    a = np.random.uniform(0, 37)
    x = int(a // 1)
    print(f'выпало число - {x}')
    if st == x:
        print('ваша ставка выиграла !!!   :-)')
        print ()
    elif x == 0:
        print('Зеро! Выигрыш казино')
        print()
    else:
        print('ваша ставка проиграла')
        print ()