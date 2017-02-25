# Сгенерировать список размером 10х10 с помощью функции задания 1
# 3.2. Заменить все четные числа на 1, не четные на 0

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
# c заменой всех четных чисел на 1, не четных на 0
def print_list_2(d2_array):
    for i in range(len(d2_array)):
        for j in range(len(d2_array)):
            if (d2_array[i][j] % 2) == 0:
                print(' 1 ', sep=' ', end=' ')
            else:
                print(' 0 ', sep=' ', end=' ')
        print()

# создать матрицу размером 10х10
matrix = gen_list(10)

print(' печать матрицы размером 10х10 ')
print_list(matrix)
print()

print('печать матрицы c заменой всех четных чисел на 1, не четных на 0')
print_list_2(matrix)
print()

print('end')