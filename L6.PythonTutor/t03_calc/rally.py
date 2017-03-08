# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршут длиной m километров?
# Программа получает на вход числа n и m.

import math

while True:
    n = int(input('Км. за день: '))
    m = int(input('Длина маршрута: '))

    print('Кол-во дней маршрута (math.ceil - округление): ', math.ceil(m/n))
    print('Кол-во дней маршрута (round - округление): ', round(m/n))

    if input('anykey - continue; 0 - stop:' ) == '0':
        break