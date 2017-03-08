# Множество '{}' в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
# 2 вида множеств:
#  - set - изменяемые - можем динамически добвалять объекты
#  - frozenset - неизменяемые
# - frozenset - мб елементом set-множества (изменяемого)

empty_frozenset = frozenset()
print(empty_frozenset)
l = list(range(10))
print(l)
my_frozenset = frozenset(l)
print(my_frozenset)

# мб елементом изменяемого множества
my_set = set(my_frozenset)
print(my_set)

# options
print(frozenset('abc').union(frozenset('cdef')))    # correct
print(frozenset('abc') | frozenset('cdef'))         # correct
print(frozenset('abc').union('cdef'))               # correct
#print(frozenset('abc') | 'cdef')                    # error. TypeError: unsupported operand type(s) for |: 'frozenset' and 'str'
