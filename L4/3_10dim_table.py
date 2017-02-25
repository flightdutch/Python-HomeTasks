# Сгенерировать список размером 10х10 с помощью функции задания 1
# 1. Заменить по главной диагонали все числа на 0
# 2. Заменить все четные числа на 1, не четные на 0
# 3. Вывести строку таблицы с максимальной суммой элементов
# 4. Повернуть таблицу на 90 градусов, по часовой, против часовой

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
                print(' 0 ',sep=' ', end= ' ')
            else:
                print(d2_array[i][j],sep=' ', end= ' ')
        print()

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

# Вывести строку таблицы с максимальной суммой элементов
def print_list_3(d2_array):
    _max = 0
    n_string_max = 0
    for i in range(len(d2_array)):
        s = 0
        for j in range(len(d2_array)):
            s += d2_array[i][j]
        if s > _max:
            _max = s
            n_string_max = i
    print(d2_array[n_string_max])


# создать матрицу размером 10х10
matrix = gen_list(10)

print(' печать матрицы размером 10х10 ')
print_list(matrix)
print()

print('печать матрицы c заменой по главной диагонали всех чисел на 0')
print_list_1(matrix)
print()

print('печать матрицы c заменой всех четных чисел на 1, не четных на 0')
print_list_2(matrix)
print()

print('печать строки таблицы с максимальной суммой элементов')
print_list_3(matrix)

print('end')