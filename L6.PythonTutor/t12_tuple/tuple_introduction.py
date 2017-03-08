# tuple - Кортеж, по сути - неизменяемый список.
# кортеж защищен от изменений, как намеренных (что плохо), так и случайных (что хорошо).
# Кортежи используется для представления неизменяемой последовательности разнородных объектов.

# Create tuple
a = tuple()                 # пустой кортеж
print('empty', a)
a = (1,)
print(a)
a = 2,
print(a)
a = tuple(range(10))
print(a)
print()
a = (1, 2, 3, 4, 5, 6)
print('tuple', a)
print('len tuple:',a.__sizeof__())

l = [1, 2, 3, 4, 5, 6]
print('list', l)
print('len string:',l.__sizeof__())

# преобразование tuple <=> list
l = list('123456789')
print(l)
t = tuple(l)
print(t)

# использовать кортежи в качестве ключей словаря:
print()
d = {(1, 1, 1) : 1}
print('tuple-dictionary',d)

print(id(d))
print(type(d))

# Распаковка кортежа
iterable = list('1234567890')
print(iterable)
# a, b, c = iterable error
a, b, *c = iterable
print(a, b, c)
head, *middle, tail = iterable
print(head, tail)
for i, value in enumerate(iterable):
    print(i, value)

print()
# tuple - doen't have generator
t = [a**2 for a in range(10)]
print(t)
t = {a**2 for a in range(10)}
print(t)
t = (a**2 for a in range(10)) # кортеж - не создается
print(t)