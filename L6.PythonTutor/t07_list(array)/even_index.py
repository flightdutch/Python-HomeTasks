# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

while True:
    a = input('numbers & spaces: ').split()

    for i in range(len(a)):
        if i % 2 == 0:
            print(a[i], end=' ')

    print()

    if input('anykey - continue; 0 - stop:') == '0':
        break