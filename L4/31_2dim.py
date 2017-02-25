# Сгенерировать список размером 10х10 с помощью функции задания 1
# 3.1. Заменить по главной диагонали все числа на 0

import random

# Сгенерировать матрицу размером 10х10
def gen_list(index):
    d2_array = []
    for i in range(index):
      d2_array.append([random.randint(100, 999) for i in range(index)])
    return d2_array

# печать матрицы размером 10х10
def print_list(d2_array):
    for i in range(len(d2_array)):
        print([d2_array[i][j] for j in range(len(d2_array)) ] )

# печать матрицы размером 10х10
# c заменой по главной диагонали всех чисел на 0
def print_list_1(d2_array):
    for i in range(len(d2_array)):
        for j in range(len(d2_array)):
            if i == j:
                print(' 0 ', sep=' ', end=' ')
            else:
                print(d2_array[i][j], sep=' ', end=' ')
        print()

# создать матрицу размером 10х10
matrix = gen_list(10)

print(' печать матрицы размером 10х10 ')
print_list(matrix)
print()

print('печать матрицы c заменой по главной диагонали всех чисел на 0')
print_list_1(matrix)
print()
