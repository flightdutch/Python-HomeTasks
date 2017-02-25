# 3.0 Сгенерировать список размером 10х10 с помощью функции задания 1
# 3.4 Повернуть таблицу на 90 градусов, по часовой, против часовой

import random

# Сгенерировать квадратную матрицу любого размера
def gen_list(index):
    d2_array = []
    for i in range(index):
      d2_array.append([random.randint(100, 999) for i in range(index)])
    return d2_array

# печать квадратной матрицы любого размера
def print_list(d2_array):
    for row in d2_array:
        print([j for j in row])


# печать повернутой на 90 градусов матрицы - против часовой
def print_list_turn_90(d2_array):
    for i in range(len(d2_array)-1, -1, -1):
        print([d2_array[j][i] for j in range(len(d2_array))])


# печать повернутой на 90 градусов матрицы - против часовой
def print_list_turn90(d2_array):
    for i in range(len(d2_array)):
        row = [d2_array[j][i] for j in range(len(d2_array))]
        print([row[j] for j in range(len(row)-1, -1, -1)])

# создать матрицу размером 10х10
matrix = gen_list(10)

print(' Контрольная печать квадратной матрицы')
print_list(matrix)
print()
print('печать повернутой на 90 градусов матрицы - против часовой')
print_list_turn_90(matrix)
print()

print('печать повернутой на 90 градусов матрицы - по часовой')
print_list_turn90(matrix)