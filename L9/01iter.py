items = (1, 2, 3, 4, 5, 6, 7)     # tuple() - кортеж
# items = [1, 2, 3, 4, 5, 6, 7]       # list
# items = '1234567'                   # string
# items = {1, 2, 3, 4, 5, 6, 7}       # set()  Множество-"контейнер", содержащий не повторяющиеся элементы в случайном порядке.
# items = {1: None, 2: None, 3: None, 4: None}      # dictionary


# for item in items:
#     print(item)

it = iter(items)
print(it)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

