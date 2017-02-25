# функция, которая генерирует список списков (двух мерный массив) размерности NxN
# заполненный случайными числами от 100 до 999
# (использовать функцию random.randint(100, 999)
import random

def gen_list(index):
    d2_array = []
    for i in range(index):
      d2_array.append([random.randint(100, 999), random.randint(100, 999)])
    return d2_array


array = gen_list(10)
print(array)