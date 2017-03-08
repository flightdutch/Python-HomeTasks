# По данному целому числу N
# распечатайте все квадраты натуральных чисел, не превосходящие N,
# в порядке возрастания.

while True:
    N = int(input('N: '))

    i = 1
    while i ** 2 <= N:
        print('Number: {}; Square: {};'.format(i, i ** 2))
        i += 1

    if input('anykey - continue; 0 - stop:') == '0':
        break