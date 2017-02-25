# функция, которая определяет количество разрядов введенного целого числа.
def n_digit(n):
    return len(str(n))

while True:
    n = input('Enter your Number: ')
    l = n_digit(n)
    print('{} have {} digits'.format(n,l))
    r = input('If you want to stop it - press 0: ')
    if r =='0':
        break
print('End')
