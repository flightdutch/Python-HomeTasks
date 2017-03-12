# тест вложенности елементов
# словари: часто используемая структура - формат JSON хорошо читается всеми языками
# users_doc = {
#     'users' : [
#         {'name': 'elias', 'age': 12},
#         {'name': 'kate', 'age': 22}
#     ]
# }
# print(users_doc['users'][0]['name'])

# изменить словарь - к каждому объекту добавить новый ключ
# добавить во все члены списка users значения 'alive': True
# for user in users_doc['users']:
#     user['alive'] = True
# print(users_doc)

# {'a': 1, 'c': 2, 'b': 4, 'g': 4}
# a 1
# b 4
# c 2
# g 4


document = {
    'date_1': '21-01-2001',
    'date_4': '21-05-2001',
    'date_0': '21-03-2001',
    'text': 'text text, text',
    'title': 'test document',
    'user': {
              'id':1,
              'name': 'elias',
              'mail': 'el@ml.ru'},
    'doc_id': 215354,
    'size': 50
}

# просмотреть все ключи
print('show keys')
for key in document.keys():
    print(key)

print()

# .keys(), .items(), .values() - меняются динамически - словарь отслеживает все изменения: добавить, обновить, удалить

# показать все значения ключей - dic.keys()
print('1. show key:element')
for key in document.keys():
    print(key, document[key])

print()

# упроащаем через dictionary.items() - возвращает пару: ключ-значение
print('2. show key:element (use items)')
for key, value in document.items():
    print(key, value)

print()

# выведем только значения - dit.values()
print('show only elements ')
for value in document.values():
    print(value)

print()


# Вывести в порядке возрастания ключей

sorted_list = list(document.keys())
sorted_list.sort()

for key in sorted_list:
    print(key, document[key])