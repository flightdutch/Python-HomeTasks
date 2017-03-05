# Дано целое число, не меньшее 2.
# Выведите его наименьший натуральный делитель, отличный от 1.

while True:
    N = int(input('N: '))

    i = 2
    while i <= N and N % i != 0:    # если данные условия не подходят, то
        i += 1                      # переход к следующему делителю
    else:                           # в противном случае,
        print(i)                    # выводится текущий делитель
        print('Number: {}; Min Divisor: {};'.format(N, i))

    if input('anykey - continue; 0 - stop:') == '0':
        break