# Заданы две клетки шахматной доски.
# Если они покрашены в один цвет, то выведите слово YES,
# а если в разные цвета — то NO.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки
# сначала для первой клетки, потом для второй клетки.

while True:
    x1 = int(input('x1: '))
    y1 = int(input('y1: '))
    x2 = int(input('x2: '))
    y2 = int(input('y2: '))

    cell1 = (x1 + y1) % 2
    cell2 = (x2 + y2) % 2

    if (cell1 == cell2):
        if cell1 == 0:
            print('Cells are white')
        else:
            print('Cells are black')
    else:
        print('Color Cells are not equal')


    if int(input('Continue - 1; Finish - 0: ')) == 0:
        break
