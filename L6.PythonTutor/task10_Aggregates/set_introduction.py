# Множество '{}' в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
# 2 вида множеств:
#  - set - изменяемые - можем динамически добвалять объекты
#  - frozenset - неизменяемые
# Множество задается перечислением всех его элементов в фигурных скобках.
# Исключением явлеется пустое множество, которое можно создать при помощи функции set().
# Если функции set передать в качестве параметра список, строку или кортеж,
# то она вернёт множество, составленное из элементов списка, строки, кортежа.
#
# Применение:
# - удаление дубликатов (почтовые рассылки)

#
# create simple set
empty_set = set()
print('empty_set',empty_set)

print('set - range:', set(range(10)))

print('Множество задается перечислением')
A = {1, 2, 3}
print(A)
A = set('qwerty')
print(A)
print()

# типа генератор - для множества
print('set - generator')
number_list = [ i+j for i in range(10) for j in range(5)]
print('number list',number_list)
number_set = { i+j for i in range(10) for j in range(5)}
print('number set',number_set)
char_set = {x for x in 'abcdgfqryteaibocp' if x not in 'abc'}
print('char set',char_set)
print()

# Каждый элемент может входить в множество только один раз, порядок задания элементов неважен.
print('Каждый элемент может входить в множество только один раз')
A = {1, 2, 3}
B = {3, 2, 3, 1}
print(A == B)
C = set('Hello')
print(A)
print(B)
print(C)
print()

################
# Работа с элементами множеств
# Узнать число элементов в множестве можно при помощи функции len.
# Перебрать все элементы множества (в неопределенном порядке!) можно при помощи цикла for

print('Работа с элементами множеств')
# Узнать число элементов в множестве можно при помощи функции len.
C = set('Hello')
print('len C:', len(C))
print()

# Перебрать все элементы множества (в неопределенном порядке!) можно при помощи цикла for
print('for - Перебрать все элементы множества! (в неопределенном порядке!)')
primes = {2, 3, 5, 7, 11}
for num in primes:
    print(num)

# Проверить, принадлежит ли элемент множеству можно при помощи операции in, возвращающей значение типа bool.
# Аналогично есть противоположная операция not in.
# Для добавления элемента в множество есть метод add
A = {1, 2, 3}
print(A)
print(1 in A, 4 not in A)
A.add(4)
print(A)
print()

# Для удаления элемента x из множества есть два метода: discard и remove.
# Их поведение различается только в случае, когда удаляемый элемент отсутствует в множестве.
# В этом случае метод discard не делает ничего, а метод remove генерирует исключение KeyError.
# Наконец, метод pop удаляет из множества один случайный элемент и возвращает его значение.
# Если же множество пусто, то генерируется исключение KeyError.
# Из множества можно сделать список при помощи функции list.
print('from list to aggregate')
l = list(range(10))
print('list',l)
print('aggregate', set(l))
print()

print('from aggregate to list')
print(A)
print(list(A))

# Убрать дубликаты в списке - если не важен порядок
a = [1,2,3,4,2,3,4,2,3,4]
print(a)
la=set(a)
print(la)
a = list(la)
print(a)
# brief optins
a = [1,2,3,4,2,3,4,2,3,4]
a = list(set(a))    # удалить дубликаты - если порядое не важен
print(a)

# change set's
my_set = {1,3,5}
print(my_set)
my_set.update({2,3,4})          # my_set |= {2,3,4}
print(my_set)
my_set.intersection_update({0,1,2,3,10})    # my_set &= {0,1,2,3,10} add many elements
print(my_set)
my_set.difference_update({1})               # my_set -= {1}
print(my_set)
my_set.symmetric_difference_update({3,4})   # my_set ^= {3,4}
print(my_set)
my_set.add(5)   # my_set |= {5}  - add only 1 element
print(my_set)
my_set.remove(2)    # my_set -= {2} но выбрасывет KeyError если не находит
print(my_set)
my_set.discard(2)   # my_set -2 {2}   НЕ выбрасывет KeyError
print(my_set)

print(my_set.pop()) # удаляет елемент (случайный) и показывает - возвращает для  использования
my_set.update({0,4,10,3,1,13})
print(my_set)
# print(my_set.pop(2))  # для множества - не работает
print([1,2,3,4,5,6,7].pop(2))  # работает для list/string - показывает  елемент по индексу

print(my_set)
my_set.clear() # очистить множество - получает пустой set
print(my_set)
