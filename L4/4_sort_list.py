#4. Написать функцию сортировки списка (любым алгоритмом)

import random

def create_list(i_len_list):
    return [random.randint(100, 999) for i in range(i_len_list)]

# Пузырьковая сортировка
def sort_list_0(_list):
    n = 1
    while n < len(_list):
        for i in range(len(_list) - n):
            if _list[i] > _list[i + 1]:
                _list[i], _list[i + 1] = _list[i + 1], _list[i]
        n += 1
    return (_list.copy())

def sort_list_1(_list):
      return sorted(_list)

def sort_list_2(_list):
    _list.sort()
    return _list

def show_list(_list):
    print(_list)


def main():
    a = create_list(10)

    print('Исходный список')
    show_list(a)
    print()

    print('Работает пузырьковая сортировка')
    show_list(sort_list_0(a.copy()))
    print()

    print('Работает функция sorted()')
    show_list(sort_list_1(a.copy()))
    print()

    print('Работает функция list.sort()')
    show_list(sort_list_2(a.copy()))

main()