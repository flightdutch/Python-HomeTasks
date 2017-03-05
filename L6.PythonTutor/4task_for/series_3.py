# Даны два целых числа A и В, A>B.
# Выведите все нечётные числа от A до B включительно, в порядке убывания.
# В этой задаче можно обойтись без инструкции if.

while True:
    A = int(input('a: '))
    B = int(input('b: '))

    if A % 2 == 0:
        for i in range(A - 1, B - 1, -2):
            print(i, end=', ')
    else:
        for i in range(A, B - 1, -2):
            print(i, end=', ')
    print()

    if input('anykey - continue; 0 - stop: ') == '0':
        break
