# First variant.
# Заданы две клетки шахматной доски.
# Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки
# сначала для первой клетки, потом для второй клетки.


while True:
    x1 = int(input('x1: '))
    y1 = int(input('y1: '))
    x2 = int(input('x2: '))
    y2 = int(input('y2: '))

    if (x1 + y1) % 2 == 0:
        print('Cell {} {} is white'.format(x1,y1))
    else:
        print('Cell {} {} is black'.format(x1, y1))

    if (x2 + y2) % 2 == 0:
        print('Cell {} {} is white'.format(x2, y2))
    else:
        print('Cell {} {} is black'.format(x2, y2))

    if (input('Continue - anykey; Finish - 0: ')) == '0':
        break
