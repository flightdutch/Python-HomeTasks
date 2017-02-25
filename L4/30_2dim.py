# 3.0 Сгенерировать список размером 10х10 с помощью функции задания 1


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

# создать матрицу размером 10х10
matrix = gen_list(10)

print(' печать матрицы размером 10х10 ')
print_list(matrix)
print()