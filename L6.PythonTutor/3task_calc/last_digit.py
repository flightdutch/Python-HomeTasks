# Дано натуральное число.
# Выведите его последнюю цифру.

while True:
    n = int(input('n: '))

    print('последнюя цифра: ', n % 10)

    if input('anykey - continue; 0 - stop:' ) == '0':
        break