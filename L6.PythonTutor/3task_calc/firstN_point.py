# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки.

while True:
    s = input('R: ')

    # n_point = s.find('.')
    # n1_after_point = s[n_point + 1]

    print('1-я цифра после точки: ', s[(s.find('.')) + 1])

    if input('anykey - continue; 0 - stop:' ) == '0':
        break