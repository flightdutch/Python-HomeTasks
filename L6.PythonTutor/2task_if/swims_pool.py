# Яша плавал в бассейне размером N × M метров и устал.
# В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков
# (не обязательно от ближайшего) и y метров от одного из коротких бортиков.
# Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик?
# Программа получает на вход числа N, M, x, y.
# Программа должна вывести число метров, которое нужно проплыть Яше до бортика.

while True:
    N = int(input('N: '))
    M = int(input('M: '))
    x = int(input('x: '))
    y = int(input('y: '))

    if N < M:
        Long, Small = M, N
    else:
        Long, Small = N, M

    a = min([x, y, (Long - y), (Small - x) ])
    print('Min distance is: ', a)

    if input('anykey - continue; 0 - stop:' ) == '0':
        break
