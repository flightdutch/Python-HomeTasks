# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
# Выведите показатель степени и саму степень.
# Операцией возведения в степень пользоваться нельзя!

while True:
    N = int(input('N: '))

    rate, r = 0, 0
    li, i = 0, 0
    while True:
        i += 1
        r = 2 ** i
        if r <= N:
            rate = r
            li = i
        else:
            break

    print('Показатель степени: {}; Степень 2: {};'.format(li, rate))

    if input('anykey - continue; 0 - stop:') == '0':
        break