#функцию is_prime(a) - принимает число и возвращает True или False
# в зависимости от того, простое это число или нет
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            print('{} % {} = {}'.format(n, i, n % i))
            return False
    return True

while True:
    n = int(input('Enter integer N: '))
    print(is_prime(n))
    if input('Do you stop cicle? enter 0:') == '0':
        break
print('End')