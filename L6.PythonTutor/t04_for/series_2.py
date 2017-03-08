# Даны два целых числа A и В.
# Выведите все числа от A до B включительно, в порядке возрастания,
# если A < B, или в порядке убывания в противном случае.

while True:
    A = int(input('a: '))
    B = int(input('b: '))

    if A < B:
        for i in range(A, B + 1, 1):
            print(i, end=', ')
    else:
        for i in range(A, B - 1, -1):
            print(i, end=', ')
    print()

    if input('anykey - continue; 0 - stop:') == '0':
        break
