# функция, которая выводит двухмерный список в виде таблицы

import random

# генератор 2-х мерных массивов
def gen_list(index):
    d2_array = []
    for i in range(index):
      d2_array.append([random.randint(100, 999), random.randint(100, 999)])
    return d2_array

# печать 2-мерных массивов в виде таблицы
def print_list(d2_array):
    print('-' * 13)
    for i in range(len(d2_array)):
        s1 = str(d2_array[i][0])
        s2 = str(d2_array[i][1])
        print('| ' + s1 + ' | ' + s2 + ' |' )

    print('-' * 13)

print_list(gen_list(10))