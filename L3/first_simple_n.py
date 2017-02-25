# Вывести на экран 10 первых простых чисел

def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            print('{} % {} = {}'.format(n, i, n % i))
            return False
    return True

n = 1
i = 1
while True:
    if is_prime(n):
        print('Simple Number N {} : {}'. format(i, n))
        i += 1
    n += 1
    if i > 10:
        break
print('End')

