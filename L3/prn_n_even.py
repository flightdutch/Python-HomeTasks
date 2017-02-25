#  функция, которая выводит на экран n первых четных чисел.

def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False

def show_n_even():
    your_n = int(input('Enter your favorite Number: '))
    n = 1
    for i in range(1, your_n+1):
        if is_even(i):
            print('{}. Even Number: {}'.format(n, i))
            n += 1
    print('Your number finished')

show_n_even()
