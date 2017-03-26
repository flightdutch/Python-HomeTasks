# Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу.
#
# https://www.tutorialspoint.com/python/python_dictionary.htm
#
# Словарь (хэш, предопределенный массив) – изменяемая структура данных,
# предназначенная для хранения элементов вида ключ: значение.
#
# Их иногда ещё называют ассоциативными массивами или хеш-таблицами.
# Создать его можно несколькими способами.

# Во-первых, с помощью литерала:
d={}
print(d)
d = {'dict': 1, 'dictionary': 2}
print(d)

# Во-вторых, с помощью функции dict:
d = dict(short='dict', long='dictionary')
print(d['short'])

# В-третьих, с помощью метода fromkeys:
d = dict.fromkeys(['a', 'b'])
print(d)
d = dict.fromkeys(['a', 'b'], 100)
print(d)

# В-четвертых, с помощью генераторов словарей, которые очень похожи на генераторы списков.
d = {a: a ** 2 for a in range(7)}
print(d)
# range(0, 6, 2)
for i in range(0, len(a) - 1, 2):
    b[a[i]] = a[i+1]

print(b)

# 2
b = {a[i]: a[i+1] for i in range(0, len(a) - 1, 2)}
print(b)

# 3
b = dict(zip(a[::2], a[1::2]))
print(b)

#  словарь - извлечь значения ключей:
d = {1: 2, 2: 4, 3: 9}
print(d)
print('dictionary - d[1]:',d[1])

# добавить записей в словарь
d[4] = 4 ** 2
print(d)

print()
# Реальное применение словаря: массив словарей
users = [
    {'name':'elias', 'age':12 },
    {'name':'kate', 'age':21 },
]
for key in users[0]:
    print(key)          # ключи в Питоне 3.5 - упорядочены. как созданы - так и обрабатываются
print()

for user in users:
    print(user['name'])
    print(user['age'])

# elias = {'name':'elias', 'age':12 }
# print(elias['name'])


# Dictionary: Options
user = {}   # create empty
user['name'] = 'elias'
user['age'] = 20
print(user)
del user['name'] # удаляем по ключу значение
print(user)

user['name'] = 'Kate'   # перезаписывать значение
print(user)
print('Kate' in user.values()) # искать значение

# Если итерировать словарь - по умолчание - подставляется значение ключа
for i in user:  # аналог - user.keys()
    print(i)

# user. - PyCharm покажет все методы объекта
user2 = user        # копируем ссылку
print(user2)
user['name'] = 'Jeka'
print(user)

# use user.copy()
user3 = user.copy()        # копируем ссылку
print('user',user)
print('user3',user3)
user3['name'] = 'Sola'
print('user',user)
print('user3',user3)