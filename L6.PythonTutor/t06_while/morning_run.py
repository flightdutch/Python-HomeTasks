# В первый день спортсмен пробежал x километров,
# а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
# По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
# Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.


while True:
    x = int(input('В 1-й день км: '))
    y = int(input('Не больше км за 1 день: '))

    n = 1
    while x < y:
        x = x + (0.1 * x)
        n += 1

    print('Кол-во дней: {}; в последний день км: {};'.format(n, x))

    if input('anykey - continue; 0 - stop:') == '0':
        break