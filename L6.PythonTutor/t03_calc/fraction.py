# Дано положительное действительное число X.
# Выведите его дробную часть.

while True:
    R= float(input('R: '))

    r1_fr = round((R % 1),2)
    print('Полный вывод дробной части: ',R % 1)
    print('Округленный вывод дробной части: ', r1_fr)

    if input('anykey - continue; 0 - stop:' ) == '0':
        break