# список будет состоять из строк, а не из чисел
# на вход подаётся строка
# 1 2 3
# s = input('string with space: ')  # s == '1 2 3'
s = '1 2 3 4 5 6'
print(s)
a = s.split()  # a == ['1', '2', '3']
print(a)
# simple list
print('simple - list/range',list(range(10)))

# получить список именно из чисел, то можно затем элементы списка по одному преобразовать в числа:
# a = input('number with space: ').split()
a = '1 2 3 4 5 6 78 88 99'.split()
print('input - a.split',a)
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

#list generater
#a = [int(s) for s in input('number with space: ').split()]
#print(a)

# диалог создания массива
# a = [0] * int(input('размер массива: '))
a = [0,0,0,0]
for i in range(len(a)):
    # a[i] = int(input('значение элемента: '))
    a[i] = (i+1)**2
print('диалог создания: ',a)

# пример, демонстрирующий использование цикла for в ситуации,
# когда из строки надо выбрать все цифры и сложить их в массив как числа.
# дано: s = 'ab12c59p7dq'
# надо: извлечь цифры в список digits,
# чтобы стало так:
# digits == [1, 2, 5, 9, 7]

s = 'ab12c59p7dq'
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print('string to int array: ', digits)

#  требуется просто вывести все элементы списка в одну строку или по одному элементу в строке.
a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    print(a[i])
a = [1, 2, 3, 4, 5]
for elem in a:
    print(elem, end=' ')
print()
# join()
a = ['red', 'green', 'blue']
print(' '.join(a))
# вернёт red green blue
print(''.join(a))
# вернёт redgreenblue
print('***'.join(a))
# вернёт red***green***blue

# Если же список состоит из чисел, то придется использовать еще тёмную магию генераторов.
# Вывести элементы списка чисел, разделяя их пробелами, можно так:
a = [11, 22, 33]
print(' '.join([str(i) for i in a]))
# следующая строка, к сожалению, вызывает ошибку:
# print(' '.join(a))

# list sort
my_list = [3,5,1,9,4,2]
print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)


