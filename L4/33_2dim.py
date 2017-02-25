# Сгенерировать список размером 10х10 с помощью функции задания 1
# 3.3. Вывести строку таблицы с максимальной суммой элементов

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
             print('Варианты максимума. № строки: ' + str(n_string_max) + ' Сумма: ' + str(_max) )
    print()
    print(d2_array[n_string_max])


# создать матрицу размером 10х10
matrix = gen_list(10)

print(' печать матрицы размером 10х10 ')
print_list(matrix)
print()

print('печать строки таблицы с максимальной суммой элементов')
print_list_3(matrix)

print('end')