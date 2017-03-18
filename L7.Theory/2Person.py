"""
Person Class
"""
class Person:
    max_age = 120

# Создает объект alex - екземпляр класса Person
alex = Person()
# Созадем атрибуты объекта (переменные)
alex.name = 'Alex'
alex.age = 17

# class работает по принципу словаря:
#  - если чего то нет - добавить
# - если это уже есть - изменить
kate = Person()
kate.name = 'Kate'
kate.age = 16

print('Kate', kate)
print(kate.name, 'is', kate.age)
print(alex.name, 'is', alex.age)

print(kate.name, 'is: ', kate.age, 'max: ', kate.max_age)
print(alex.name, 'is: ', alex.age, 'max: ', alex.max_age)

# Проверка - оба производных класса ссылаються на один и тотже атрибут одного и того же класса
print(kate.max_age is alex.max_age)

# Атрибуты экземпляра
kate.a = 'test'
# сначала атрибут ищется в текущем экземпляре класса
print(kate.a)
# если в текущем экземпляре класса его нет - поиск поднимается на ступень выще в производный класс
print(kate.max_age)
kate.max_age = 130
print(kate.max_age)
# атрибуты - разные
print(kate.max_age is alex.max_age)